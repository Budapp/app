from django.contrib import admin
from django.utils.html import format_html

from budapp.helpers import url as url_helper
from budapp.apps.core.fields.models import Field
from .models import (
    Table,
)


class FieldInline(admin.TabularInline):
    model = Field
    fk_name = 'table'


class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'go_to_create_model_form')
    search_fields = ('name', 'description',)
    list_filter = ('name',)
    inlines = [FieldInline]
    fieldsets = (
        ('Información básica', {
            'fields': ('name', 'description',)
        }),
    )

    def go_to_create_model_form(self, obj):
        obj_url = url_helper.get_url_by_name(
            'budapp_model_create_document',
            ** {'pk': obj.pk})
        return format_html(
            f'<a href="{obj_url}" target="_blank">Click to change</a>')

    go_to_create_model_form.allow_tags = True


admin.site.register(Table, TableAdmin)
