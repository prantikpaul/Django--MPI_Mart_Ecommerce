# Generated by Django 4.2.7 on 2023-11-25 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_alter_product_avg_rating_star'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='avg_rating_star',
        ),
    ]
