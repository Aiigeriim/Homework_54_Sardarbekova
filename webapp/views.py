from django.shortcuts import render, redirect, get_object_or_404


from webapp import models
from webapp.forms import ProductForm, SearchForm
from webapp.models import Category, Product


def index(request):
    products = models.Product.objects.filter(rest__gt=0).order_by('-category', 'title')
    return render(request, 'index.html', {'products': products})



def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            price = form.cleaned_data.get('price')
            image = form.cleaned_data.get('image')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            rest = form.cleaned_data.get('rest')
            product = Product.objects.create(rest=rest, title=title, price=price, image=image, category=category,
                                             description=description)
            return redirect('product_detail', pk=product.pk)
        else:
            return render(request, 'create_product.html', {"form": form})
    else:
        form = ProductForm()
        categories = Category.objects.all()
        return render(request, 'create_product.html', context={"form": form, "categories": categories})




def add_category(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = Category.objects.create(title=title, description=description)
        return redirect('index')
    else:
        return render(request,'create_category.html')
def detail(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail_product.html', {'product': product})

def update_product(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product.title = form.cleaned_data.get('title')
            product.description = form.cleaned_data.get('description')
            product.category = form.cleaned_data.get('category')
            product.rest = form.cleaned_data.get('rest')
            product.price = form.cleaned_data.get('price')
            product.image = form.cleaned_data.get('image')
            product.save()
            return redirect('product_detail', pk=product.pk)
        else:
            return render(request, 'update_product.html', {'form': form})
    else:
        form = ProductForm(initial={'title': product.title, 'description': product.description, 'category': product.category, 'rest': product.rest, 'price': product.price, 'image': product.image})
        return render(request, 'update_product.html', {'form': form})


def delete_product(request, *args, pk, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("index")
    else:
        return render(request, 'delete_product.html', {"product": product})