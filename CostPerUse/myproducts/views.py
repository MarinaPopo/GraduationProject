from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from django.core.paginator import Paginator
from .forms import CategoryForm, ProductForm


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


@login_required(login_url="login")
def create_category(request):
    # profile = request.user.profile
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            # project.owner = profile
            form.save()
            return redirect('my_products')

    context = {'form': form}
    return render(request, 'myproducts/create-category.html', context)


@login_required(login_url="login")
def create_product(request):
    # profile = request.user.profile
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            # project.owner = profile
            form.save()
            return redirect('my_products')

    context = {'form': form}
    return render(request, 'myproducts/create-product.html', context)



