from django.forms import ModelForm, widgets, DateField
from django import forms
from .models import Category, Product


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price', 'category', 'date_created']
        widgets = {
            'date_created': widgets.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control py-4'
    #     self.fields['image'].widget.attrs['class'] = "custom-file-input"


    def __init__(self, *args, user=None, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['category'].queryset = Category.objects.filter(user=user)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


