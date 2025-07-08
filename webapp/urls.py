from django.urls import path

from webapp.views import detail, index, add_product, add_category, update_product

urlpatterns = [
    path('', index, name='index'),
    path('products/', index, name='index'),
    path('products/<int:pk>/', detail, name='product_detail'),
    path('products/add/', add_product, name='add_product'),
    path('categories/add/', add_category, name='add_category'),
    path('product/<int:pk>/update/', update_product, name='update_product'),
]