# Generated by Django 5.1.1 on 2024-11-14 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0088_remove_slide_material_source_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='lab_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
