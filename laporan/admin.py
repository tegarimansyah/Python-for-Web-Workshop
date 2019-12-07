from django.contrib import admin
from django.utils.html import format_html

from .models import Laporan, Komentar, Vote

class LaporanAdmin(admin.ModelAdmin):
    # =================================
    # Display Configuration
    # =================================
    date_hierarchy = 'timestamp'

    list_display = (
        'timestamp',
        '__str__',
        'pelapor',
        'kategori',
        'status',
        'lihat_map'
    )
    def lihat_map(self, obj):
        return format_html(
            f'<a href="https://www.google.com/maps/place/{obj.kecamatan}">\
            Lihat Map\
            </a>')

    list_editable = ('status',)

    search_fields = ('judul', 'deskripsi')
    list_filter = ('timestamp', 'status')

    # =================================
    # Add or Change Form Configuration
    # =================================

    fields = (
        'timestamp',
        'pelapor',
        'judul',
        'deskripsi',
        'kecamatan',
        'kategori',
     )
    # exclude = ('status',)
    readonly_fields = ('timestamp',)

admin.site.register(Laporan, LaporanAdmin)
admin.site.register(Komentar)
admin.site.register(Vote)