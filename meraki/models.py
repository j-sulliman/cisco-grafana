from django.db import models
from django.utils import timezone

class Organizations(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    last_updated = models.DateTimeField(default=timezone.now)


class MerakiNetworks(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    organizationId = models.CharField(max_length=200)
    productTypes = models.CharField(max_length=200)
    timeZone = models.CharField(max_length=200)
    last_updated = models.DateTimeField(default=timezone.now)

class MerakiDevices(models.Model):
    serial = models.CharField(max_length=200, primary_key=True)
    address = models.CharField(max_length=200)
    mac = models.CharField(max_length=200)
    lanIp = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200)
    networkId = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    firmware = models.CharField(max_length=200)
    wan1Ip = models.CharField(max_length=200, null=True)
    wan2Ip = models.CharField(max_length=200, null=True)
    last_updated = models.DateTimeField(default=timezone.now)
