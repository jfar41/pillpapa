# Generated by Django 3.1.1 on 2020-09-20 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emergencycontact',
            name='patient',
        ),
    ]
