# Generated by Django 3.0.8 on 2021-03-13 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v0', '0005_auto_20210313_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='user_id',
            new_name='user',
        ),
    ]
