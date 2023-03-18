# Generated by Django 4.1.7 on 2023-03-17 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='books.book')),
            ],
            options={
                'verbose_name': 'Recommendation',
                'verbose_name_plural': 'Recommendations',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='previews', to='books.book')),
            ],
            options={
                'verbose_name': 'Preview',
                'verbose_name_plural': 'Previews',
                'ordering': ['id'],
            },
        ),
    ]
