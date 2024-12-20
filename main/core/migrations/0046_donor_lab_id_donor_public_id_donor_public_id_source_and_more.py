# Generated by Django 5.1.1 on 2024-10-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_rename_id_panel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='lab_id',
            field=models.CharField(default='blah', max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donor',
            name='public_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='donor',
            name='public_id_source',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='panel',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slides',
            name='name',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='panel',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='slides',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
