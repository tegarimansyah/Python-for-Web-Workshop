from django.db import models
from django.contrib.auth.models import User

class Kecamatan(models.Model):
    def __str__(self):
        return self.nama
    nama = models.CharField(max_length=50)
    # laporan

class Kategori(models.Model):
    def __str__(self):
        return self.nama
    nama = models.CharField(max_length=50)
    # laporan
    # kedinasan

class Kedinasan(models.Model):
    def __str__(self):
        return self.nama
    nama = models.CharField(max_length=50)
    kategori = models.ManyToManyField(Kategori, related_name='kedinasan')


class InformasiTambahanUser(models.Model):
    def __str__(self):
        return self.user.get_full_name()
    user    = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pegawai")
    nik     = models.CharField(max_length=20, blank=True, null=True)
    telepon = models.CharField(max_length=15, blank=True, null=True)
    kecamatan = models.ForeignKey(Kecamatan, on_delete=models.CASCADE, related_name='user', blank=True, null=True)
    kedinasan = models.ForeignKey(Kedinasan, on_delete=models.CASCADE, related_name='pegawai', blank=True, null=True)