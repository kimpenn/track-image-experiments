# Generated by Django 5.1.1 on 2024-10-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_sitesettings_probe_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='probe_types',
            field=models.JSONField(default=dict),
        ),
    ]
