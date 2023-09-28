from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.CharField(blank=True, max_length=200, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, verbose_name='Название')
    image = models.ImageField(upload_to='products_images/', blank=True, verbose_name='Изображение')
    description = models.CharField(max_length=250, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    times = models.PositiveIntegerField(default=0, blank=True, verbose_name='Количество раз')
    date_created = models.DateTimeField(blank=True, null=True, verbose_name='Дата покупки')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Категория')
    is_archived = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'
