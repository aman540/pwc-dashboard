# Generated by Django 4.0.4 on 2022-07-04 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_rename_semester_project_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Associate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('joindate', models.DateField(auto_now_add=True, null=True)),
                ('occupency', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateField(auto_now=True, null=True)),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.technology')),
            ],
        ),
    ]