# Generated by Django 3.1.1 on 2020-09-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosing',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
