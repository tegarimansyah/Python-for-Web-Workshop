from django.db import models

class AdditionalUserData(models.Model):
    nama        = models.CharField(max_length=20)
    nik         = models.CharField(max_length=20, blank=True, null=True)
    daerah      = models.CharField(max_length=25, blank=True, null=True)
    telepon     = models.CharField(max_length=15, blank=True, null=True)
    dinas       = models.CharField(max_length=20, blank=True, null=True)

class Kedinasan(models.Model):
    nama        = models.CharField(max_length=50)