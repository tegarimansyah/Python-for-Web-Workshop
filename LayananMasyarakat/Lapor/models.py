from django.db import models

# Create your models here.
class Laporan(models.Model):
    INBOX = 1
    RESPOND = 2
    ON_PROGRESS = 3
    DONE = 4

    status_choices = (
        (INBOX, 'Telah Diterima'),
        (RESPOND, 'Respon'),
        (ON_PROGRESS, 'Sedang Dikerjakan'),
        (DONE, 'Selesai')
    )

    waktu       = models.DateTimeField(auto_now_add=True)
    judul       = models.CharField(max_length=160)
    deskripsi   = models.TextField(blank=True, null=True)
    status      = models.SmallIntegerField(choices=status_choices, default=INBOX)

    kecamatan   = models.CharField(max_length=50)
    kategori    = models.CharField(max_length=50)

class Komentar(models.Model):
    waktu       = models.DateTimeField(auto_now_add=True)
    name        = models.CharField(max_length=50)
    isi         = models.TextField()
    laporam     = models.IntegerField()

class Vote(models.Model):
    UP_VOTE = 1
    DOWN_VOTE = 0

    vote_choices = (
        (UP_VOTE, 'Saya setuju'),
        (DOWN_VOTE, 'Saya tidak setuju')
    )

    nama        = models.CharField(max_length=50)
    laporan     = models.IntegerField()
    pilihan     = models.BooleanField(choices=vote_choices)

class Kategori(models.Model):
    nama        = models.CharField(max_length=50)
    kedinasan   = models.CharField(max_length=50)