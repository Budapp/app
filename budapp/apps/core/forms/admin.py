from django.contrib import admin
from django.utils.html import format_html

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
        return format_html('<a href="">Click to change</a>')
    go_to_form_page.allow_tags=True



admin.site.register(Form, FormAdmin)
admin.site.register(FormField)
