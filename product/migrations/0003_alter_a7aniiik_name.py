# Generated by Django 4.1.7 on 2023-02-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_products_a7aniiik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a7aniiik',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
