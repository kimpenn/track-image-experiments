# Generated by Django 5.1.1 on 2024-10-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_flourescentmolecules_imagingsuccessoptions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='probe',
            name='fluorescent_molecule',
            field=models.CharField(choices=[], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='probe',
            name='imaging_success',
            field=models.CharField(choices=[], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='probe',
            name='probe_panel_id',
            field=models.CharField(choices=[], max_length=30, null=True),
        ),
    ]
