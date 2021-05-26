from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class dnac_network_device(models.Model):
    dnac_addr = models.CharField(max_length=200)
    mgt_ip = models.CharField(max_length=200)
    assoc_wlc = models.CharField(max_length=200)
    up_time_sec = models.BigIntegerField()
    device_support_level = models.CharField(max_length=200)
    sw_type = models.CharField(max_length=200)
    sw_ver = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    interface_count = models.CharField(max_length=200)
    line_card_count = models.CharField(max_length=200)
    platform_id = models.CharField(max_length=200)
    ser_number = models.CharField(primary_key=True, max_length=200)
    role = models.CharField(max_length=200)
    instance_tenant_id = models.CharField(max_length=200)
    id = models.CharField(max_length=200)
    reachability_status = models.CharField(max_length=200)
    manageability = models.CharField(max_length=200)
    mac = models.CharField(max_length=200)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.switch_name


class dnac_site_health(models.Model):
    dnac_addr = models.CharField(max_length=200)
    siteName = models.CharField(max_length=200)
    siteId = models.CharField(max_length=200)
    parentSiteId = models.CharField(max_length=200, null=True)
    siteType = models.CharField(max_length=200, null=True)
    healthyNetworkDevicePercentage = models.IntegerField(null=True)
    clientHealthWired = models.IntegerField(null=True)
    clientHealthWireless = models.IntegerField(null=True)
    numberOfClients = models.IntegerField(null=True)
    numberOfNetworkDevice = models.IntegerField(null=True)
    networkHealthAverage = models.IntegerField(null=True)
    networkHealthAccess = models.IntegerField(null=True)
    networkHealthCore = models.IntegerField(null=True)
    networkHealthDistribution = models.IntegerField(null=True)
    networkHealthRouter = models.IntegerField(null=True)
    networkHealthAP = models.IntegerField(null=True)
    networkHealthWLC = models.IntegerField(null=True)
    networkHealthSwitch = models.IntegerField(null=True)
    networkHealthWireless = models.IntegerField(null=True)
    networkHealthOthers = models.IntegerField(null=True)
    numberOfWiredClients = models.IntegerField(null=True)
    numberOfWirelessClients = models.IntegerField(null=True)
    wiredGoodClients = models.IntegerField(null=True)
    wirelessGoodClients = models.IntegerField(null=True)
    overallGoodDevices = models.IntegerField(null=True)
    accessGoodCount = models.IntegerField(null=True)
    accessTotalCount = models.IntegerField(null=True)
    coreGoodCount = models.IntegerField(null=True)
    coreTotalCount = models.IntegerField(null=True)
    distributionGoodCount = models.IntegerField(null=True)
    distributionTotalCount = models.IntegerField(null=True)
    routerGoodCount = models.IntegerField(null=True)
    routerTotalCount = models.IntegerField(null=True)
    wirelessDeviceGoodCount = models.IntegerField(null=True)
    wirelessDeviceTotalCount = models.IntegerField(null=True)
    apDeviceGoodCount = models.IntegerField(null=True)
    apDeviceTotalCount = models.IntegerField(null=True)
    wlcDeviceGoodCount = models.IntegerField(null=True)
    wlcDeviceTotalCount = models.IntegerField(null=True)
    switchDeviceGoodCount = models.IntegerField(null=True)
    switchDeviceTotalCount = models.IntegerField(null=True)
    applicationHealth = models.IntegerField(null=True)
    applicationGoodCount = models.IntegerField(null=True)
    applicationTotalCount = models.IntegerField(null=True)
    applicationBytesTotalCount = models.IntegerField(null=True)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.switch_name

class dnac_issues(models.Model):
    dnac_addr = models.CharField(max_length=200)
    issueId = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    siteId = models.CharField(max_length=200)
    deviceId = models.CharField(max_length=200)
    deviceRole = models.CharField(max_length=200)
    aiDriven = models.CharField(max_length=200)
    clientMac = models.CharField(max_length=200)
    issue_occurence_count = models.IntegerField( null=True)
    status = models.CharField(max_length=200)
    priority = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    last_occurence_time = models.DateTimeField(primary_key=True, max_length=200)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.switch_name
