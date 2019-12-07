from django.db import models
from django.contrib.auth.models import User

from masterdata.models import Kecamatan, Kategori

class Laporan(models.Model):
    INBOX = 1
    RESPOND = 2
    ON_PROGRESS = 3
    DONE = 4
    STATUS_CHOICES = (
        (INBOX, 'Sudah Masuk'),
        (RESPOND, 'Ditanggapi'),
        (ON_PROGRESS, 'Sedang Dikerjakan'),
        (DONE, 'Selesai')
    )

    pelapor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="laporan")
    timestamp = models.DateTimeField('Waktu Submit', auto_now_add=True)
    judul = models.CharField(max_length=50)
    deskripsi = models.TextField(blank=True, null=True)
    kecamatan = models.ForeignKey(Kecamatan, on_delete=models.CASCADE, related_name="laporan")
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name="laporan")
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    
    # komentar
    # vote
    
    def __str__(self):
        return self.judul[:20] + '...'

class Komentar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="komentar")
    laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE, related_name='komentar')   
    komentar = models.TextField(max_length=1024)

class Vote(models.Model):
    UP_VOTE = 1
    DOWN_VOTE = 0
    VOTE_CHOICES = (
        (UP_VOTE, 'Setuju'),
        (DOWN_VOTE, 'Tidak Setuju')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vote")
    laporan = models.ForeignKey(Laporan, on_delete=models.CASCADE, related_name='vote')
    vote = models.BooleanField(choices=VOTE_CHOICES)