# Generated by Django 5.1.1 on 2024-10-21 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_organregions_organs_slides_species_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probe',
            name='probe_type',
            field=models.CharField(choices=[('DAPI', 'DAPI'), ('H&E', 'H&E'), ('Antibody', 'Antibody'), ('smFISH', 'smFISH'), ('something', 'something')], default='', max_length=30, null=True),
        ),
    ]
