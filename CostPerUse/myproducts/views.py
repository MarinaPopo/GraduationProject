from django.shortcuts import render, redirect

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
        products = Product.objects.filter(category_id=category_id, user=user, is_archived=False)

    else:
        products = Product.objects.filter(user=user, is_archived=False)


    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({'products': page_obj})
    return render(request, 'myproducts/myproducts.html', context)

@login_required(login_url='/')
def archive(request):
    user = request.user
    context = {
        'title': 'Архив',
        'categories': Category.objects.filter(user=user),
    }
    products = Product.objects.filter(user=user, is_archived=True)

    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({'products': page_obj})
    return render(request, 'myproducts/archive.html', context)


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

    context = {'form': form, 'title': 'Создать категорию'}
    return render(request, 'myproducts/create-category.html', context)


@login_required(login_url="login/")
def create_product(request):
    user = request.user
    form = ProductForm(user=request.user)
    categories = Category.objects.filter(user=user)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = user
            form.save()
            return redirect('my_products')

    context = {'form': form, 'categories': categories, 'title': 'Добавить товар'}
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
    if product.times >= 1:
        product.times -= 1
        product.save()

    return redirect(current_page)


@login_required(login_url='/')
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('my_products')
    return render(request, 'myproducts/delete-product.html', {'product': product})


@login_required(login_url='/')
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('my_products')
    return render(request, 'myproducts/delete-category.html', {'category': category})


@login_required(login_url='/')
def add_to_archive(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.is_archived = True
        product.save()
        return redirect('my_products')

    return render(request, 'myproducts/add-to-archive.html', {'product': product})

@login_required(login_url='/')
def restore_from_archive(request, product_id):
    product = Product.objects.get(id=product_id)
    product.is_archived = False
    product.save()
    return redirect('my_products')



@login_required(login_url='/')
def product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('my_products')
    else:
        form = ProductForm(instance=product)

    context = {
        'title': product.name,
        'product': product,
        'categories': Category.objects.all(),
        'form': form,
    }
    return render(request, 'myproducts/product.html', context)