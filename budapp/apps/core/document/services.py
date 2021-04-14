from budapp.exceptions import document as documentExceptions

from .models import Document, DocumentValue


def get_document(**kwargs):
    try:
        return Document.objects.get(**kwargs)
    except (Document.DoesNotExist, Document.MultipleObjectsReturned):
        return None


def create(**kwargs):
    return Document.objects.create(**kwargs)


def create_value(**kwargs):
    return DocumentValue.objects.create(**kwargs)
