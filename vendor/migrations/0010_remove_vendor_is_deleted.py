# Generated by Django 4.2.6 on 2023-10-10 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0009_vendor_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='is_deleted',
        ),
    ]
