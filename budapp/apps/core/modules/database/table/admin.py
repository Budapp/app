from django.contrib import admin

from .models import (
    Table,
)


class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)
    list_filter = ('name',)

    fieldsets = (
        ('Información básica', {
            'fields': ('name', 'description',)
        }),
    )


admin.site.register(Table, TableAdmin)
