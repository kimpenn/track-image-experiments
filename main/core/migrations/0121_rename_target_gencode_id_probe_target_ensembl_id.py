# Generated by Django 5.1.1 on 2024-12-04 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0120_rename_flourescentmolecules_capturechannel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='probe',
            old_name='target_gencode_id',
            new_name='target_ensembl_id',
        ),
    ]
