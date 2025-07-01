

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', unique=True)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Продукт')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey('webapp.Category', on_delete=models.RESTRICT, verbose_name='Категория', related_name='products')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.URLField(max_length=300, verbose_name='Картинка')

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
