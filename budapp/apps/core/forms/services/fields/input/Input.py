from django import forms

from ..Field import Field

FIELD_TYPE_MAP = {
    'text': forms.CharField
}


class Input(Field):
    widget = forms.PasswordInput()

    def render(self):
        return FIELD_TYPE_MAP[self.field.input_type](**self._get_field_attrs())
