from django.core.management.base import BaseCommand, CommandError

from budapp.apps.core.table.models import Table
from budapp.apps.core.fields.models import Field

SUCCESS_MESSAGE = 'All data deleted.'


class Command(BaseCommand):
    help = 'Delete data to develop environment'

    def handle(self, *args, **kwargs):
        Table.objects.all().delete()
        Field.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(SUCCESS_MESSAGE))
