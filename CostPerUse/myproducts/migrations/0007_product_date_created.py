# Generated by Django 4.2.2 on 2023-09-21 10:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myproducts', '0006_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата покупки'),
            preserve_default=False,
        ),
    ]