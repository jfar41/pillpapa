# Generated by Django 3.1.1 on 2020-09-24 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20200924_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='pill',
            name='qty_remaining',
            field=models.IntegerField(default=273),
        ),
    ]
