from django.contrib import admin
from .models import Laporan, Komentar, Vote
# Register your models here.

class LaporanAdmin(admin.ModelAdmin):
    list_display = (
        'waktu',
        'judul',
        'deskripsi',
        'status',
        'kecamatan',
        'kategori',
    )

    list_editable = (
        'status',
        'kategori',
    )

admin.site.register(Laporan, LaporanAdmin)
admin.site.register(Komentar)
admin.site.register(Vote)
