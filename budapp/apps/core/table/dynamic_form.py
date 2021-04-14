from django import forms
from django.core.exceptions import ValidationError

from budapp.apps.core.table.services import table as table_services
from budapp.apps.core.forms.services.FormGenerator import FormGenerator
from budapp.apps.core.document import services as document_service


class CreateModelDocumentForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(CreateModelDocumentForm, self).__init__(*args, **kwargs)
        table_id = kwargs['initial']['pk']
        self.table = table_services.get_table(**{'pk': table_id})

        self.table_fields = self.table.fields.all()
        self.fields = FormGenerator(
            self.table_fields).generate_fields()

    def _parse_fields_by_name_dict(self):
        fields_by_name = {}
        for field in self.table_fields:
            fields_by_name[field.name] = field
        return fields_by_name

    def create_document(self):
        fields_by_name = self._parse_fields_by_name_dict()
        document_created = document_service.create(**{
            'table': self.table,
        })

        for field_name, field_instance in fields_by_name.items():
            document_service.create_value(**{
                'document': document_created,
                'field': field_instance,
                'value': self.cleaned_data[field_name],
            })
