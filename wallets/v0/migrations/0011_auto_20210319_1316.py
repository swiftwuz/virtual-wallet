# Generated by Django 3.0.8 on 2021-03-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v0', '0010_auto_20210318_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(),
        ),
    ]