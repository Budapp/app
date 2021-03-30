from django.contrib import admin

from .models import (
    Field,
)


class FieldAdmin(admin.ModelAdmin):
    list_display = ('table', 'name',  'element', 'input_type',
                    'description', 'required', 'unique',)
    search_fields = ('name', 'description', 'element',
                     'input_type',)
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
   
        ('Validation configuration', {
            'fields': ('required', 'unique',)
        }),
        ('Relational configuration', {
            'fields': (
                'table_related',
                'table_relation_type'
            ),
        }),
    )


admin.site.register(Field, FieldAdmin)
