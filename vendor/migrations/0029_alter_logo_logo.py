# Generated by Django 4.2.6 on 2023-10-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0028_alter_logo_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='logo',
            field=models.ImageField(default='assets/images/vendor_logo/default.png', upload_to='images/vendor_logo'),
        ),
    ]