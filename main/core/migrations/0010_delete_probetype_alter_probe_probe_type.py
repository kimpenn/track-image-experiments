# Generated by Django 5.1.1 on 2024-10-08 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_probe_probe_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProbeType',
        ),
        migrations.AlterField(
            model_name='probe',
            name='probe_type',
            field=models.CharField(choices=[('H&E', 'H&E'), ('DAPI', 'DAPI'), ('Antibody', 'Antibody'), ('smFISH', 'smFISH')], max_length=30, null=True),
        ),
    ]
