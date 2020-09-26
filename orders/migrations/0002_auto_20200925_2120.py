# Generated by Django 2.2 on 2020-09-25 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordereditem',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Products'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.OrderStatus'),
        ),
    ]
