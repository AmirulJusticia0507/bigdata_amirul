# Generated by Django 5.1.5 on 2025-01-20 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PemainBola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('posisi', models.CharField(max_length=50)),
                ('klub', models.CharField(max_length=100)),
                ('umur', models.IntegerField()),
            ],
        ),
    ]
