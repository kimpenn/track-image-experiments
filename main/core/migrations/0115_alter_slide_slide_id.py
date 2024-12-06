# Generated by Django 5.1.1 on 2024-11-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0114_alter_slide_slide_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='slide_id',
            field=models.CharField(blank=True, help_text='This is an unique ID for the slide. It could, for example, be the Visium slide ID.', max_length=30, null=True, unique=True, verbose_name='slide ID'),
        ),
    ]