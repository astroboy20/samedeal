# Generated by Django 4.0.2 on 2022-03-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Message', models.TextField(max_length=1000)),
            ],
        ),
    ]
