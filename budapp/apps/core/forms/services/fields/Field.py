from django import forms

from budapp.apps.core.fields.validators import common as common_validators


class Field(object):
    def __init__(self, field):
        self.field = field
        self.attrs = {
            'validators': []
        }

        self._set_required_attr()
        self._set_common_validators()

    def _validate_unique_value_if_needed(self, value):
        if self.field.unique:
            return common_validators.validate_unique_value(self.field, value)

    def _set_common_validators(self):
        self.attrs['validators'].append(
            self._validate_unique_value_if_needed
        )

    def _set_required_attr(self):
        self.attrs['required'] = self.field.required

    def _get_field_attrs(self):
        return self.attrs
