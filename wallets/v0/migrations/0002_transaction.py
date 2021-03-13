# Generated by Django 3.0.8 on 2021-03-13 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v0', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'pending'), ('FAILED', 'failed'), ('SUCCESS', 'success')], max_length=100)),
                ('transaction_type', models.CharField(choices=[('TRANSFER', 'transfer'), ('DEPOSIT', 'desposit'), ('WITHDRAWAL', 'withdrawal')], max_length=100)),
                ('sender', models.CharField(max_length=100)),
                ('recipient', models.CharField(max_length=100)),
                ('reference_id', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
    ]
