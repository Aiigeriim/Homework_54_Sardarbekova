from django.urls import path

from webapp.views import detail, index, add_product, add_category

urlpatterns = [
    path('', index, name='index'),
    path('products/<int:pk>/', detail, name='product_detail'),
    path('add-product/', add_product, name='add_product'),
    path('categories/add', add_category, name='add_category')
]