from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from django.core.paginator import Paginator
from .forms import CategoryForm, ProductForm


@login_required(login_url='/')
def my_products(request, category_id=None):
    user = request.user
    context = {
        'title': 'Мои покупки',
        'categories': Category.objects.filter(user=user),
    }

    if category_id:
        products = Product.objects.filter(category_id=category_id, user=user)

    else:
        products = Product.objects.filter(user=user)

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({'products': page_obj})
    return render(request, 'myproducts/myproducts.html', context)


@login_required(login_url="/")
def create_category(request):
    user = request.user
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = user
            form.save()
            return redirect('my_products')

    context = {'form': form}
    return render(request, 'myproducts/create-category.html', context)


@login_required(login_url="login/")
def create_product(request):
    user = request.user
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = user
            form.save()
            return redirect('my_products')

    context = {'form': form}
    return render(request, 'myproducts/create-product.html', context)


@login_required(login_url='/')
def plus_use(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    product.times += 1
    product.save()
    if product.times % 10 == 2 or product.times % 10 == 3 or product.times % 10 == 4:
        variant = 'раза'
    else:
        variant = 'раз'
    context = {'variant': variant}
    return redirect(current_page, context)


@login_required(login_url='/')
def minus_use(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    if product.times > 1:
        product.times -= 1
        product.save()
    else:
        product.times = 0
        product.save()
    return redirect(current_page)


@login_required(login_url='/')
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/')
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect(request.META.get('HTTP_REFERER'))
