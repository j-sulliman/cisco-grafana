# Generated by Django 3.2 on 2021-05-05 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcnm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcnm_network_switch',
            name='memoryUsage',
            field=models.IntegerField(max_length=200),
        ),
    ]
