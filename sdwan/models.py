from django.db import models
from django.utils import timezone

# Create your models here.
class sdwan_devices(models.Model):
    deviceId = models.CharField(max_length=200)
    system_ip = models.CharField(max_length=200)
    host_name = models.CharField(max_length=200)
    reachability = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    personality = models.CharField(max_length=200)
    device_type = models.CharField(max_length=200)
    lastupdated = models.CharField(max_length=200)
    domain_id = models.CharField(max_length=200)
    board_serial = models.CharField(primary_key=True, max_length=200)
    certificate_validity = models.CharField(max_length=200)
    site_id = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    uptime_date = models.BigIntegerField()
    validity = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    state_description = models.CharField(max_length=200)
    local_system_ip = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.board_serial


class sdwan_deviceCounters(models.Model):
    crashCount = models.IntegerField()
    expectedControlConnections = models.IntegerField()
    number_vsmart_control_connections = models.IntegerField()
    rebootCount = models.IntegerField()
    systemIp = models.CharField(max_length=200)
    bfdSessionsUp = models.IntegerField(default=None)
    bfdSessionsDown = models.IntegerField(default=None)
    ompPeersDown = models.IntegerField(default=None)
    ompPeersUp = models.IntegerField(default=None)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.systemIp
