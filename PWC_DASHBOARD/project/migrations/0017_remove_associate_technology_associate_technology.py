# Generated by Django 4.0.4 on 2022-07-04 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_associate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='associate',
            name='technology',
        ),
        migrations.AddField(
            model_name='associate',
            name='technology',
            field=models.ManyToManyField(to='project.technology'),
        ),
    ]
