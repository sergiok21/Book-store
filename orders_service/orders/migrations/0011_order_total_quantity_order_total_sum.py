# Generated by Django 4.1.7 on 2023-04-05 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_extra_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_sum',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]