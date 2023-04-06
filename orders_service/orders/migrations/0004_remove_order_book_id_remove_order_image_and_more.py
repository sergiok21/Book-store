# Generated by Django 4.1.7 on 2023-03-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_id_alter_order_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='image',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user_id',
        ),
        migrations.AddField(
            model_name='order',
            name='extra_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
