from django.contrib import admin

from .models import (
    Form,
    FormField,
)


# class FormFieldInline(admin.TabularInline):
#     model = FormField


class FormAdmin(admin.ModelAdmin):
    # inlines = [FormFieldInline]
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)
    list_filter = ('name',)
    fieldsets = (
        ('Información básica', {
            'fields': ('name', 'description',)
        }),

    )


admin.site.register(Form, FormAdmin)
admin.site.register(FormField)
