from django.contrib import admin
from .models import Laporan, Komentar, Kategori, District, Vote, Custom_user
# Register your models here.

@admin.register(Laporan, Komentar, Kategori, District, Vote, Custom_user)
class AuthorAdmin(admin.ModelAdmin):
    pass