# Generated by Django 3.0.8 on 2021-03-18 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v0', '0008_auto_20210313_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
