# Generated by Django 5.1.1 on 2024-10-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0077_alter_probe_probe_panel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probe',
            name='probe_panel',
            field=models.ManyToManyField(related_name='probes', to='core.panel'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='probe_panel',
            field=models.ManyToManyField(related_name='panels', to='core.panel'),
        ),
    ]
