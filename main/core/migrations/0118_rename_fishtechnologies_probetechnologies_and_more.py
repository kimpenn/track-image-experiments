# Generated by Django 5.1.1 on 2024-12-04 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0117_alter_sample_slice_index'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FishTechnologies',
            new_name='ProbeTechnologies',
        ),
        migrations.AlterModelOptions(
            name='probetechnologies',
            options={'verbose_name_plural': 'probe technologies'},
        ),
        migrations.RenameField(
            model_name='probe',
            old_name='fish_technology',
            new_name='probe_technology',
        ),
    ]
