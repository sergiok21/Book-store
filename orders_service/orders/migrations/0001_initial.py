# Generated by Django 4.1.7 on 2023-03-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField(default=0)),
                ('book_id', models.PositiveIntegerField(default=0)),
                ('order_number', models.CharField(blank=True, max_length=64, null=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('image', models.URLField(blank=True, max_length=512, null=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
