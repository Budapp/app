from .fields.FieldLoader import FieldLoader


class FormGenerator(object):
    def __init__(self, fields):
        self.fields = fields

    def render_field(self, field):
        field_loader = FieldLoader(field)
        
        return field_loader.load()


    def generate_fields(self):
        fields_rendered = {}
        for field in self.fields:
            fields_rendered[field.name] = self.render_field(field)

        return fields_rendered
