# Generated by Django 5.1.1 on 2024-10-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_probe_fluorescent_molecule_probe_imaging_success_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='sex',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other'), ('N', 'Not reported'), ('U', 'Unknown')], default='U', max_length=1),
        ),
        migrations.AlterField(
            model_name='probe',
            name='fish_technology',
            field=models.CharField(choices=[('smHCR', 'smHCR'), ('HCR', 'HCR'), ('Sellaris', 'Sellaris'), ('inHouse', 'inHouse'), ('hiFISH', 'hiFISH'), ('Oligopaint', 'Oligopaint'), ('Not applicable', 'Not applicable')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='probe',
            name='fluorescent_molecule',
            field=models.CharField(choices=[('DAPI', 'DAPI'), ('GFP', 'GFP'), ('Alexa Flour 488', 'Alexa Flour 488')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='probe',
            name='imaging_success',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Adjust working dilution', 'Adjust working dilution')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='probe',
            name='probe_panel_id',
            field=models.CharField(choices=[('H&E', 'H&E'), ('DAPI', 'DAPI'), ('Test panel', 'Test panel'), ("Jean's FISH panel", "Jean's FISH panel")], max_length=30, null=True),
        ),
    ]
