# Generated by Django 3.1.5 on 2021-01-19 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StockStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_items', models.IntegerField(blank=True, null=True)),
                ('ordered_count', models.IntegerField(blank=True, null=True)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='Cafeteriacore.item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.BooleanField(default=False)),
                ('order_id', models.IntegerField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Cafeteriacore.item')),
            ],
        ),
        migrations.CreateModel(
            name='ExtendedUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('employee_id', models.CharField(blank=True, max_length=250, null=True)),
                ('organization', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extended_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
