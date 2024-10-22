# Generated by Django 5.1.1 on 2024-10-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_remove_probe_probe_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='probe',
            name='probe_type',
            field=models.CharField(choices=[('DAPI', 'DAPI'), ('H&E', 'H&E'), ('Antibody', 'Antibody'), ('smFISH', 'smFISH'), ('something', 'something')], max_length=30, null=True),
        ),
    ]
