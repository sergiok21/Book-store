# Generated by Django 4.1.7 on 2023-03-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_book_id_remove_order_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
