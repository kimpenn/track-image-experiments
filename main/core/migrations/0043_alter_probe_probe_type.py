# Generated by Django 5.1.1 on 2024-10-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_alter_probe_probe_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probe',
            name='probe_type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
