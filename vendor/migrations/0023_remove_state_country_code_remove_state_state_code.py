# Generated by Django 4.2.6 on 2023-10-17 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0022_country_phonecode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='state',
            name='state_code',
        ),
    ]
