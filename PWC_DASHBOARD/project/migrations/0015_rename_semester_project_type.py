# Generated by Django 4.0.4 on 2022-07-04 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_project_semester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='semester',
            new_name='type',
        ),
    ]
