# Generated by Django 2.1.7 on 2020-04-14 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flea_market', '0005_auto_20200414_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type_category',
            field=models.CharField(choices=[('CAT', 'Категория'), ('SUBCAT', 'Подкатегория')], default='CAT', max_length=10),
        ),
    ]
