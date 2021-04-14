from django.core.exceptions import ValidationError

from budapp.apps.core.document import services as document_service


def validate_unique_value(field, value):
    print("Validating unique field, ", field, value)
    query = {
        'table': field.table,
        'documentvalue__field': field,
        'documentvalue__value': value,
        'deleted_at__isnull': True,
    }

    document_created = document_service.get_document(**query)
    if document_created:
        raise ValidationError('This field is unique.')
