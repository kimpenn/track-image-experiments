# Generated by Django 5.1.1 on 2024-10-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_delete_probetype_delete_probetypes_probe_probe_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProbeType',
            fields=[
                ('type', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]