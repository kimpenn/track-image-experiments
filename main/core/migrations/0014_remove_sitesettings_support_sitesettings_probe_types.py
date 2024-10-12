# Generated by Django 5.1.1 on 2024-10-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_sitesettings_remove_probe_fish_technology_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='support',
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='probe_types',
            field=models.JSONField(default='["H&E", "DAPI", Antibody", "smFISH"]'),
        ),
    ]