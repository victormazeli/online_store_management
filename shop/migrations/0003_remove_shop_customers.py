# Generated by Django 2.2 on 2020-09-25 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200925_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='customers',
        ),
    ]