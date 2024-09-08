from django.contrib import admin
from .models import CpInputModel

class CpInputModelAdmin(admin.ModelAdmin):
    list_display = ( 'id',
        'mp_jumlah', 'mp_pos', 'material_jumlah', 'material_std', 
        'mesin_normal', 'metode_sesuai', 'plan_vs_actual', 'environment_aman', 
        'tanggal_check', 'person'
    )
    list_filter = ('tanggal_check', 'person')  # Optional: add filters
    search_fields = ('person__username',)  # Optional: search by username

    fieldsets = (
        (None, {
            'fields': ('mp_jumlah', 'mp_pos', 'material_jumlah', 'material_std',
                       'mesin_normal', 'metode_sesuai', 'plan_vs_actual',
                       'environment_aman', 'person')
        }),
    )
    #readonly_fields=('tanggal_check',)


admin.site.register(CpInputModel, CpInputModelAdmin)