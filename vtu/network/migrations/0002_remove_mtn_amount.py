# Generated by Django 4.0.2 on 2022-03-28 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtn',
            name='amount',
        ),
    ]