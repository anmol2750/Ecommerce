# Generated by Django 4.2.6 on 2023-10-10 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_vendor_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='code',
        ),
    ]
