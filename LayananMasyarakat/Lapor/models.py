from django.db import models

# Create your models here.
class Laporan(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=5000)
    status = models.CharField(max_length=25)
    kategori = models.CharField(max_length=50)
    datetime = models.DateTimeField()

class Komentar(models.Model):
    isi = models.CharField(max_length=500)
    datetime = models.DateTimeField()

class Vote(models.Model):
    pilihan = models.CharField(max_length=100)

class District(models.Model):
    nama = models.CharField(max_length=25)

class Kategori(models.Model):
    nama = models.CharField(max_length=50)

class Custom_user(models.Model):
    nik = models.CharField(max_length=20)
    daerah = models.CharField(max_length=25)
    telepon = models.CharField(max_length=15)
    jabatan = models.CharField(max_length=20)
