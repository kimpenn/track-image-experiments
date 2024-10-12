# Generated by Django 5.1.1 on 2024-10-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_panel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='microscope',
            name='json_description',
            field=models.FileField(blank=True, null=True, upload_to='hardware_json/'),
        ),
        migrations.AlterField(
            model_name='panel',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='panel',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='panel',
            name='probe_list',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]