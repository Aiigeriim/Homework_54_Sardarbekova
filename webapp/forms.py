from django import forms
from django.forms import widgets

from webapp.models import Category, Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=100,
        required=True,
        label="Название",
        widget=widgets.Input(
        attrs={'class': 'form-control'}),
        error_messages={"required": "Пожалуйста, введите название"},),
    description = forms.CharField(
        widget=forms.Textarea(
        attrs={"cols": "25", "rows": "5", "class": "form-control"}),
        required=False,
        label="Описание"),
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        widget=forms.Select(attrs={'class': 'form-control'})
    ),
    rest = forms.IntegerField(min_value=0, label='Остаток'),
    price = forms.DecimalField(decimal_places=2, max_digits=7, label='<Цена'),
    image = forms.URLField(max_length=300, label='Картинка')

    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'rest', 'price', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'rest': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }




