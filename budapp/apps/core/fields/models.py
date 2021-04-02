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
        related_name='fields')
    name = models.CharField(u'Name', max_length=50)
    description = models.TextField(u'Description', null=True, blank=True)
    required = models.BooleanField('Required', default=False)
    unique = models.BooleanField('Unique', default=False)
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
    table_relation_type = models.CharField(
        'Table relation type',
        choices=RELATIONAL_TYPES,
        max_length=20,
        null=True,
        blank=True,
        default='foreign_key')

    def __str__(self):
        return f'table: {self.table} - {self.name} ({self.element})'
