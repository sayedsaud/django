# Generated by Django 5.0.7 on 2024-08-01 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('firstapp', '0001_initial'),
        ('secondapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
                ('project_status', models.CharField(max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.client')),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.emp')),
            ],
        ),
    ]
