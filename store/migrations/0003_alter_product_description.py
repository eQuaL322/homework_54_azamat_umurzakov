# Generated by Django 4.1.7 on 2023-02-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_remove_category_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', max_length=2000, null=True, verbose_name='Описание'),
        ),
    ]
