from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class openvuln_advisory(models.Model):
    advisoryId = models.CharField(primary_key=True, max_length=200)
    advisoryTitle = models.TextField(max_length=200)
    bugIDs = models.TextField()
    cves = models.TextField()
    cvrfUrl = models.TextField()
    cvssBaseScore = models.FloatField()
    cwe = models.CharField(max_length=200)
    firstPublished = models.DateTimeField(max_length=200)
    ipsSignatures = models.CharField(max_length=200)
    lastUpdated = models.DateTimeField(max_length=200)
    productNames = models.TextField()
    publicationUrl = models.TextField()
    sir = models.TextField()
    status = models.CharField(max_length=200)
    summary = models.TextField()
    devicesImpacted = models.CharField(max_length=200, default='no')
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.advisoryId
