from django.db import models

from budapp.constants.fields import (
    FIELD_INPUT_TYPES,
    FIELD_ELEMENTS,
)
from budapp.constants.table import RELATIONAL_TYPES


class Field(models.Model):
    table = models.ForeignKey(
        'table.Table',
        on_delete=models.CASCADE,
        related_name='table')
    name = models.CharField(u'Name', max_length=50)
    label = models.CharField(u'Label', max_length=100)
    help_text = models.CharField(
        u'Help text', max_length=100, blank=True, null=True)
    description = models.TextField(u'Description', null=True, blank=True)
    required = models.BooleanField('Required', default=False)
    unique = models.BooleanField('Unique', default=False)
    order = models.IntegerField('Order', default=0)
    element = models.CharField(
        'Element',
        choices=FIELD_ELEMENTS,
        max_length=20,
        null=True,
        blank=True,
        default='input')
    input_type = models.CharField(
        'Type',
        choices=FIELD_INPUT_TYPES,
        max_length=20,
        null=True,
        blank=True,
        default='text')

    # For relational table -> fields
    table_related = models.ForeignKey(
        'table.Table',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='table_related')
    table_field_related = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='table_field_related_related')
    table_relation_type = models.CharField(
        'Table relation type',
        choices=RELATIONAL_TYPES,
        max_length=20,
        null=True,
        blank=True,
        default='foreign_key')

    def __str__(self):
        return f'table: {self.table} - {self.name} ({self.element})'
