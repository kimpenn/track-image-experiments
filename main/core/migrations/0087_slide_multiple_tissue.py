# Generated by Django 5.1.1 on 2024-11-14 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0086_alter_slide_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='multiple_tissue',
            field=models.BooleanField(default=False),
        ),
    ]
