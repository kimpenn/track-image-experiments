# Generated by Django 5.1.1 on 2024-10-22 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_rename_option_fishtechnologies_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probe',
            name='probe_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.probetypes'),
        ),
    ]
