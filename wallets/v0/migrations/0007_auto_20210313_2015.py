# Generated by Django 3.0.8 on 2021-03-13 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v0', '0006_auto_20210313_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactionevent',
            old_name='wallet_id',
            new_name='wallet',
        ),
    ]
