# Generated by Django 5.1.1 on 2024-11-22 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0102_alter_assay_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assay',
            options={'verbose_name_plural': 'Assays'},
        ),
    ]
