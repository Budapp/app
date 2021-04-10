from django import forms


class Field(object):
    def __init__(self, field):
        self.field = field
        self.attrs = {}

        self._set_required_attr()

    def _set_required_attr(self):
        self.attrs['required'] = self.field.required

    def _get_field_attrs(self):
        import ipdb;ipdb.set_trace()
        print()
        
        return self.attrs
