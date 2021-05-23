# Generated by Django 3.2 on 2021-05-17 04:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sdwan_devices',
            fields=[
                ('deviceId', models.CharField(max_length=200)),
                ('system_ip', models.CharField(max_length=200)),
                ('host_name', models.CharField(max_length=200)),
                ('reachability', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('personality', models.CharField(max_length=200)),
                ('device_type', models.CharField(max_length=200)),
                ('lastupdated', models.CharField(max_length=200)),
                ('domain_id', models.CharField(max_length=200)),
                ('board_serial', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('certificate_validity', models.CharField(max_length=200)),
                ('site_id', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('uptime_date', models.BigIntegerField()),
                ('validity', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('state_description', models.CharField(max_length=200)),
                ('local_system_ip', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=200)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]