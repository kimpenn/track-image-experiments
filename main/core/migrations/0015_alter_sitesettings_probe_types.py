# Generated by Django 5.1.1 on 2024-10-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_sitesettings_support_sitesettings_probe_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='probe_types',
            field=models.JSONField(default="['H&E', 'DAPI', Antibody', 'smFISH']"),
        ),
    ]
