from django.db import models
import datetime


class Editier2api(models.Model):
    # id = models.AutoField(primary_key=True)
    description = models.TextField()
    created = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.created)


class JobFlow(models.Model):
    jobFlowName = models.CharField(max_length=50)
    intervalTime = models.FloatField()
    jobName = models.CharField(max_length=50)
    countryCode = models.CharField(max_length=10)
    created = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.jobFlowName)
