from django.db import models
from django.utils import timezone


class Document(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    table = models.ForeignKey(
        'table.Table',
        on_delete=models.CASCADE,
        related_name='table')

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return f'{self.table}'


class DocumentValue(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    value = models.TextField(blank=True, null=True)
    field = models.ForeignKey(
        'fields.Field',
        on_delete=models.CASCADE,
        related_name='field')

    class Meta:
        verbose_name = 'Document value'
        verbose_name_plural = 'Document values'

    def __str__(self):
        return f'[{self.document}]: {self.field}: {self.value}'
