# Generated by Django 4.2.7 on 2023-11-25 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_product_avg_rating_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avg_rating_star',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]