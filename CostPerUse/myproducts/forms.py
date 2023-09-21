from django.forms import ModelForm, widgets, DateField
from django import forms
from .models import Category, Product


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'input'})


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price', 'category', 'date_created']
        widgets = {
            'date_created': widgets.DateInput(attrs={'type': 'date'})
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'input'})


