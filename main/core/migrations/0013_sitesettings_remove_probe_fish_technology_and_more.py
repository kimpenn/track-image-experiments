# Generated by Django 5.1.1 on 2024-10-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_exposuretime'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('support', models.EmailField(default='support@example.com', max_length=254)),
                ('sales_department', models.EmailField(blank=True, max_length=254)),
                ('twilio_account_sid', models.CharField(default='ACbcad883c9c3e9d9913a715557dddff99', max_length=255)),
                ('twilio_auth_token', models.CharField(default='abd4d45dd57dd79b86dd51df2e2a6cd5', max_length=255)),
                ('twilio_phone_number', models.CharField(default='+15006660005', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='probe',
            name='fish_technology',
        ),
        migrations.RemoveField(
            model_name='probe',
            name='fluorescent_molecule',
        ),
        migrations.RemoveField(
            model_name='probe',
            name='imaging_success',
        ),
        migrations.RemoveField(
            model_name='probe',
            name='panel_id',
        ),
        migrations.RemoveField(
            model_name='probe',
            name='probe_type',
        ),
    ]
