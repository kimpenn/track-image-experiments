# Generated by Django 5.1.1 on 2024-10-23 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_alter_slides_options_alter_species_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fishtechnologies',
            options={'verbose_name_plural': 'fish technologies'},
        ),
        migrations.AlterModelOptions(
            name='flourescentmolecules',
            options={'verbose_name_plural': 'flourescent molecules'},
        ),
        migrations.AlterModelOptions(
            name='imagingsuccessoptions',
            options={'verbose_name_plural': 'imaging success options'},
        ),
        migrations.AlterModelOptions(
            name='organregions',
            options={'verbose_name_plural': 'organ regions'},
        ),
        migrations.AlterModelOptions(
            name='probepanels',
            options={'verbose_name_plural': 'probe panels'},
        ),
        migrations.AlterModelOptions(
            name='probetypes',
            options={'verbose_name_plural': 'probe types'},
        ),
    ]
