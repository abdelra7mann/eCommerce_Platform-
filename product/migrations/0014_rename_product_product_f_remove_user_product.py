# Generated by Django 4.1.7 on 2023-02-25 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_product_photo_alter_product_pord_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Product_F',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Product',
        ),
    ]
