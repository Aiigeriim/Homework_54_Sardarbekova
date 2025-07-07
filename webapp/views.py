from django.shortcuts import render, redirect, get_object_or_404


from webapp import models
from webapp.models import Category, Product


def index(request):
    products = models.Product.objects.all()
    return render(request, 'index.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        image = request.POST.get('image')
        description = request.POST.get('description')
        category_id = request.POST.get('category_id')
        product = Product.objects.create(title=title, price=price, image=image, category_id=category_id, description=description)
        return redirect('product_detail', pk=product.pk )
    else:
        categories = Category.objects.all()
        return render(request,'create_product.html', {'categories': categories})

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
