from django.contrib import admin
from django.utils.html import format_html

from budapp.helpers import url as url_helper

from .models import (
    Form,
    FormField,
)


class FormFieldInline(admin.TabularInline):
    model = FormField


class FormAdmin(admin.ModelAdmin):
    inlines = [FormFieldInline]
    list_display = ('name', 'description', 'go_to_form_page')
    search_fields = ('name', 'description',)
    list_filter = ('name',)
    fieldsets = (
        ('Información básica', {
            'fields': ('name', 'description',)
        }),

    )

    def go_to_form_page(self, obj):
        obj_url = url_helper.get_url_by_name(
            'budapp_model_basic_form',
            ** {'table_id': obj.pk})
        return format_html(
            f'<a href="{obj_url}" target="_blank">Click to change</a>')

    go_to_form_page.allow_tags = True


admin.site.register(Form, FormAdmin)
admin.site.register(FormField)
