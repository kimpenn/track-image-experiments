# Generated by Django 5.1.1 on 2024-10-30 13:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0080_alter_microscope_json_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceTreatments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name_plural': 'source treatments',
            },
        ),
        migrations.RemoveField(
            model_name='slide',
            name='imaging_by',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='imaging_date',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='microscope',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='probe_panel',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='staining_by',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='staining_date',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='staining_protocol',
        ),
        migrations.AddField(
            model_name='slide',
            name='source_storage_time',
            field=models.IntegerField(blank=True, help_text='How long the tissue was stored before slicing (days).', null=True),
        ),
        migrations.CreateModel(
            name='Assay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('staining_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('imaging_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('imaging_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imaging_by', to='core.people')),
                ('microscope', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.microscope')),
                ('probe_panel', models.ManyToManyField(related_name='panels', to='core.panel')),
                ('staining_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staining_by', to='core.people')),
                ('staining_protocol', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.stainingprotocols')),
            ],
            options={
                'verbose_name_plural': 'assays',
            },
        ),
        migrations.AddField(
            model_name='slide',
            name='assay',
            field=models.ManyToManyField(related_name='assays', to='core.assay'),
        ),
        migrations.AddField(
            model_name='slide',
            name='source_treatment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.sourcetreatments'),
        ),
    ]