# Generated by Django 4.1.7 on 2023-03-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_preview_image_recommendation_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
