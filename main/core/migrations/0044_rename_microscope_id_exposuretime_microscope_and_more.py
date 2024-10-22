# Generated by Django 5.1.1 on 2024-10-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_alter_probe_probe_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exposuretime',
            old_name='microscope_id',
            new_name='microscope',
        ),
        migrations.RenameField(
            model_name='exposuretime',
            old_name='probe_id',
            new_name='probe',
        ),
        migrations.AddField(
            model_name='microscope',
            name='name',
            field=models.CharField(default='something', max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='probe',
            name='name',
            field=models.CharField(default='more', max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='microscope',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='probe',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]