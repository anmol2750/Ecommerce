# Generated by Django 4.2.6 on 2023-10-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0014_address_address_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]