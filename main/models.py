from django.db import models


class MetroLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    color = models.CharField(max_length=60)


class MetroStation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    open = models.TimeField()
    close = models.TimeField()
    line = models.ForeignKey(MetroLine, on_delete=models.CASCADE)
