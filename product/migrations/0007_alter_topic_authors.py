# Generated by Django 4.1.7 on 2023-02-23 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_author_topic_author_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='authors',
            field=models.ManyToManyField(default='drama', to='product.author'),
        ),
    ]
