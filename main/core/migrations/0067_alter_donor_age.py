# Generated by Django 5.1.1 on 2024-10-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_alter_slides_donor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
