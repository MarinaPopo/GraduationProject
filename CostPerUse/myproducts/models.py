from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Категории')
    description = models.TextField(blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    image = models.ImageField(upload_to='products_images/', blank=True, verbose_name='Изображение')
    description = models.CharField(max_length=250, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    times = models.PositiveIntegerField(default=0, blank=True, verbose_name='Количество раз')
    # cost_per_use = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='Стоимость '
    #                                                                                             'использования')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'
