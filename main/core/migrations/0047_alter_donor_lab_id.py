# Generated by Django 5.1.1 on 2024-10-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_donor_lab_id_donor_public_id_donor_public_id_source_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='lab_id',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
    ]
