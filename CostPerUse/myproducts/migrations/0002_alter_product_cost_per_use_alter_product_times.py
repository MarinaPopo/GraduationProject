# Generated by Django 4.2.2 on 2023-09-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproducts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost_per_use',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='Стоимость использования'),
        ),
        migrations.AlterField(
            model_name='product',
            name='times',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Количество раз'),
        ),
    ]
