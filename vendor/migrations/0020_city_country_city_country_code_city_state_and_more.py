# Generated by Django 4.2.6 on 2023-10-16 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0019_state_country_state_country_code_state_state_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vendor.country'),
        ),
        migrations.AddField(
            model_name='city',
            name='country_code',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vendor.state'),
        ),
        migrations.AddField(
            model_name='city',
            name='state_code',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
