from django.contrib import admin

from .models import (
    Field,
)


class FieldAdmin(admin.ModelAdmin):
    list_display = ('table', 'name', 'label', 'element', 'input_type',
                    'description', 'help_text', 'required', 'unique', 'order')
    search_fields = ('name', 'description', 'element',
                     'input_type', 'help_text')
    list_filter = ('name', 'element', 'input_type',
                   'required', 'unique', 'table__name',)

    fieldsets = (
        ('Table', {
            'fields': ('table',)
        }),
        ('Basic infomation', {
            'fields': ('name', 'description',)
        }),
        ('Basic configuration', {
            'fields': ('element', 'input_type',)
        }),
        ('Display configuration', {
            'fields': ('label', 'help_text', 'order',)
        }),
        ('Validation configuration', {
            'fields': ('required', 'unique',)
        }),
    )


admin.site.register(Field, FieldAdmin)
