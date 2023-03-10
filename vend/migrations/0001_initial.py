# Generated by Django 4.1.5 on 2023-01-20 19:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import vend.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('to_rent', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Аренда')),
                ('publish', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(default=vend.models.Address.get_default_pk, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='device', to='vend.address', verbose_name='Адреса')),
            ],
            options={
                'verbose_name': 'Аппарат',
                'verbose_name_plural': 'Аппараты',
            },
        ),
        migrations.CreateModel(
            name='SensorWin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateTimeField(default=datetime.datetime(2023, 1, 20, 19, 48, 40, 120323, tzinfo=datetime.timezone.utc), verbose_name='Дата снятия счетчика')),
                ('number', models.IntegerField(default=0, verbose_name='Счетчик')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sensor_win', to='vend.device')),
            ],
            options={
                'verbose_name': 'Счетчик выигрыша',
                'verbose_name_plural': 'Счетчики выигрышей',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateTimeField(auto_now_add=True, verbose_name='Дата снятия счетчика')),
                ('number', models.IntegerField(default=0, verbose_name='Счетчик')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sensor', to='vend.device')),
            ],
            options={
                'verbose_name': 'Счетчик игр',
                'verbose_name_plural': 'Счетчики игры',
            },
        ),
    ]
