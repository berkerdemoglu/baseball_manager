# Generated by Django 3.2 on 2021-04-16 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_auto_20210416_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teams.team'),
        ),
    ]
