# Generated by Django 5.1.4 on 2025-01-07 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arabalar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Araba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200)),
                ('yil', models.IntegerField()),
                ('fiyat', models.FloatField()),
                ('resim', models.ImageField(upload_to='images')),
                ('motorhacmi', models.IntegerField(verbose_name='Araç Motor Hacmi')),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arabalar.kategori')),
            ],
        ),
    ]
