# Generated by Django 4.0.5 on 2022-06-12 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_technology_technoproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='associates',
            name='Technology',
        ),
    ]
