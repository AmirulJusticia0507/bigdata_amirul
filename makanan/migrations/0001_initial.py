# Generated by Django 5.1.5 on 2025-01-20 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Makanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tanggal_ditambahkan', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
