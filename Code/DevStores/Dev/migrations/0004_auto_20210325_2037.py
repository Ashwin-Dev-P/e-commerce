# Generated by Django 3.1.4 on 2021-03-25 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dev', '0003_customer_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_review',
            old_name='product_id',
            new_name='product',
        ),
    ]
