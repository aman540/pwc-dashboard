# Generated by Django 4.0.4 on 2022-06-13 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_remove_associates_technology'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusDurationOfProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.phase')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
    ]
