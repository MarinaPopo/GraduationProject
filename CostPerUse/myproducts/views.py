from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from django.core.paginator import Paginator


def my_products(request, category_id=None):
    context = {
        'title': 'Мои покупки',
        'categories': Category.objects.all(),
        }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({'products': page_obj})
    return render(request, 'myproducts/myproducts.html', context)


