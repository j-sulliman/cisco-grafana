# Generated by Django 3.2 on 2021-05-21 02:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='openvuln_advisory',
            fields=[
                ('advisoryId', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('advisoryTitle', models.TextField(max_length=200)),
                ('bugIDs', models.TextField()),
                ('cves', models.TextField()),
                ('cvrfUrl', models.TextField()),
                ('cvssBaseScore', models.FloatField()),
                ('cwe', models.CharField(max_length=200)),
                ('firstPublished', models.DateTimeField(max_length=200)),
                ('ipsSignatures', models.CharField(max_length=200)),
                ('lastUpdated', models.DateTimeField(max_length=200)),
                ('productNames', models.TextField()),
                ('publicationUrl', models.TextField()),
                ('sir', models.TextField()),
                ('status', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('devicesImpacted', models.CharField(default='no', max_length=200)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
