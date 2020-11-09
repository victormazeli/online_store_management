# Generated by Django 3.1.3 on 2020-11-09 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=150, null=True)),
                ('state', models.CharField(blank=True, max_length=124, null=True)),
                ('city', models.CharField(blank=True, max_length=124, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('total', models.FloatField(default=0.0)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customers')),
                ('item_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productvariation')),
                ('items', models.ManyToManyField(to='products.Products')),
            ],
        ),
    ]
