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
        image = request.FILES.get('image')
        description = request.POST.get('description')
        # created_at = request.POST.get('created_at')
        # updated_at = request.POST.get('updated_at')

        product = Product.objects.create(title=title, price=price, image=image, description=description)
        return redirect('detail.html', pk=product.pk )
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
    product = get_object_or_404(Product, id=pk)
    return render(request, 'detail.html', {'product': product})
