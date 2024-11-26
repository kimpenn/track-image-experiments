# Generated by Django 5.1.1 on 2024-11-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0096_alter_slide_options_remove_slide_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assay',
            name='slides_applied',
        ),
        migrations.AddField(
            model_name='slide',
            name='assays_used',
            field=models.ManyToManyField(blank=True, related_name='assays', to='core.assay'),
        ),
    ]