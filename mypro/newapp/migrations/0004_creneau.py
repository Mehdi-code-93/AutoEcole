# Generated by Django 5.0.5 on 2024-06-04 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_member_heurrestante_member_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creneau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
                ('moniteur', models.CharField(max_length=100)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.member')),
            ],
        ),
    ]