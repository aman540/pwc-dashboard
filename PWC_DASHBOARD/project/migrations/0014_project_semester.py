# Generated by Django 4.0.4 on 2022-07-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_project_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='semester',
            field=models.CharField(choices=[('Erp', 'Erp'), ('aws', 'aws'), ('Azure', 'Azure'), ('salesforce', 'salesforce'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=20, null=True),
        ),
    ]