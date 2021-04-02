from django import forms

from budapp.apps.core.table import services as table_services
from budapp.apps.core.forms.services.FormGenerator import FormGenerator


class CreateModelDocumentForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(CreateModelDocumentForm, self).__init__(*args, **kwargs)
        table_id = kwargs['initial']['pk']

        table = table_services.get_table(**{'pk': table_id})

        self.fields = FormGenerator(table.fields.all()).generate_fields()

