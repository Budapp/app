from .input.Input import Input


FIELD_ELEMENT_MAP = {
    'input': Input
}


class FieldLoader(object):
    def __init__(self, field):
        self.field = field

    def _validate_element(self):
        success = True
        if self.field.element not in FIELD_ELEMENT_MAP:
            print('ERROR, Elemento no existe')
            success = False

        return success

    def load(self):
        if self._validate_element():
            field_class =  FIELD_ELEMENT_MAP[self.field.element]
            field_class_instance = field_class(self.field)

            return field_class_instance.render()