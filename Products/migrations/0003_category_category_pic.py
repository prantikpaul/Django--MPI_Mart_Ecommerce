# Generated by Django 4.2.7 on 2023-11-21 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_product_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_pic',
            field=models.ImageField(default=1, upload_to='product_img/category_img/'),
            preserve_default=False,
        ),
    ]