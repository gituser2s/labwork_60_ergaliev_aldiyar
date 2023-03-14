from django import forms
from webapp.models import Product, Basket


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        count = forms.IntegerField(min_value=0)
        fields = {'title', 'description', 'photo', 'category', 'count', 'price'}
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'photo': 'Фото',
            'category': 'Категория',
            'count': 'Остаток',
            'price': 'Цена',
        }


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        count = forms.IntegerField(min_value=0)
        fields = {'product', 'count'}
        labels = {
            'product': 'Продукт',
            'count': 'Остаток',
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')

