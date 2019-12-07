from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Kecamatan, Kedinasan, Kategori, InformasiTambahanUser

admin.site.register(Kecamatan)
admin.site.register(Kedinasan)
admin.site.register(Kategori)

class InformasiTambahanUserInline(admin.StackedInline):
    model = InformasiTambahanUser
    can_delete = False
    verbose_name_plural = 'Informasi Tambahan User'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (InformasiTambahanUserInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)