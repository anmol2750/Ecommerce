# Generated by Django 4.2.6 on 2023-10-13 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0011_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]