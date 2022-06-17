# Generated by Django 4.0.5 on 2022-06-11 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_from_duration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Associates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Technology', models.CharField(blank=True, max_length=50)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.manager')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
