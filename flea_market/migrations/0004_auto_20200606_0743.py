# Generated by Django 2.1.7 on 2020-06-06 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flea_market', '0003_auto_20200606_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flea_market.Location'),
        ),
    ]
