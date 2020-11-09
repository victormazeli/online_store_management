# Generated by Django 3.1.3 on 2020-11-09 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0.0)),
                ('discounted_price', models.FloatField(default=0.0)),
                ('quantity_in_stock', models.IntegerField(default=0)),
                ('unit', models.CharField(choices=[('kg', 'kg'), ('cm', 'cm'), ('pcs', 'pcs'), ('boxes', 'boxes')], default='pcs', max_length=20)),
                ('sales', models.IntegerField(default=0)),
                ('extra_detail', models.CharField(blank=True, max_length=255, null=True)),
                ('in_stock', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0.0)),
                ('quantity', models.IntegerField(default=0)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productoption')),
            ],
        ),
        migrations.AddField(
            model_name='productoption',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]
