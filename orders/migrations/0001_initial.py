# Generated by Django 3.1.3 on 2020-11-09 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=126)),
                ('status', models.CharField(choices=[('paid', 'paid'), ('unpaid', 'unpaid'), ('open', 'open'), ('cancelled', 'cancelled')], default='open', max_length=126)),
                ('shipping_cost', models.FloatField(default=0.0)),
                ('total_cost', models.FloatField(default=0.0)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customercart')),
                ('customer_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customers')),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
    ]
