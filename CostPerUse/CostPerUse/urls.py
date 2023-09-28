"""
URL configuration for CostPerUse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from myproducts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calculator.urls')),
    path('products/', views.my_products, name='my_products'),
    path('products/archive', views.archive, name='archive'),
    path('products/<int:category_id>/', views.my_products, name='category'),
    path('products/create-category/', views.create_category, name='create_category'),
    path('products/create-product/', views.create_product, name='create_product'),
    path('products/plus-use/<int:product_id>/', views.plus_use, name='plus_use'),
    path('products/minus-use/<int:product_id>/', views.minus_use, name='minus_use'),
    path('products/delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/add-to-archive/<int:product_id>/', views.add_to_archive, name='add_to_archive'),
    path('products/restore-from-archive/<int:product_id>/', views.restore_from_archive, name='restore_from_archive'),
    path('products/delete-category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('product/<int:pk>/', views.product, name='product'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
