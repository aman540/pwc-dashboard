# Generated by Django 4.0.4 on 2022-06-13 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_statusdurationofproject'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StatusDurationOfProject',
            new_name='PhaseDurationOfProject',
        ),
    ]
