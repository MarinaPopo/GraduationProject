# Generated by Django 4.2.2 on 2023-09-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproducts', '0005_category_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Категория'),
        ),
    ]
