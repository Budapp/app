from ..models import Table


def get_table(**kwargs):
    try:
        return Table.objects.get(**kwargs)
    except (Table.DoesNotExist, Table.MultipleObjectsReturned):
        return None
