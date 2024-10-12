# Generated by Django 5.1.1 on 2024-10-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_probe_probe_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlourescentMolecules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImagingSuccessOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProbePanelIDs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SiteSettings',
        ),
        migrations.AddField(
            model_name='probe',
            name='fish_technology',
            field=models.CharField(choices=[('smHCR', 'smHCR'), ('HCR', 'HCR'), ('Sellaris', 'Sellaris'), ('inHouse', 'inHouse'), ('hiFISH', 'hiFISH')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='fishtechnologies',
            name='option',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='probe',
            name='probe_type',
            field=models.CharField(choices=[('DAPI', 'DAPI'), ('H&E', 'H&E'), ('Antibody', 'Antibody'), ('smFISH', 'smFISH')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='probetypes',
            name='option',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
