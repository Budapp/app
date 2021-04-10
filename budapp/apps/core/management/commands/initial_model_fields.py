from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from budapp.apps.core.table.models import Table
from budapp.apps.core.fields.models import Field


SUCCESS_MESSAGE = 'Successfully create data.'
USER_FIELDS = [
    {
        'name': 'name',
        'description': 'User name',
        'required': True,
        'unique': False,
        'element': 'input',
        'input_type': 'text',
    },
    {
        'name': 'email',
        'description': 'User email',
        'required': True,
        'unique': True,
        'element': 'input',
        'input_type': 'email',
    },
]

PRODUCT_FIELDS = [
    {
        'name': 'name',
        'description': 'Product name',
        'required': True,
        'unique': True,
        'element': 'input',
        'input_type': 'text',
    },
    {
        'name': 'description',
        'description': 'Product description',
        'required': False,
        'unique': False,
        'element': 'textarea',
        'input_type': 'text',
    },
]


class Command(BaseCommand):
    help = 'Create initial data to develop environment'

    # ===== User models ======
    def _create_User_model(self):
        return Table.objects.create(**{
            'name': 'User',
            'description': 'Client users profile'
        })

    def _create_User_data(self, table):
        for user_field in USER_FIELDS:
            user_field['table'] = table
            Field.objects.create(**user_field)
    # ===== [END] User models ======

    # ===== Product models ======
    def _create_Product_model(self):
        return Table.objects.create(**{
            'name': 'Product',
            'description': 'Products'
        })

    def _create_Product_data(self, table):
        for product_field in PRODUCT_FIELDS:
            product_field['table'] = table
            Field.objects.create(**product_field)
    # ===== [END] Product models ======

    @transaction.atomic
    def handle(self, *args, **kwargs):
        user_model = self._create_User_model()
        self._create_User_data(user_model)

        product_model = self._create_Product_model()
        self._create_Product_data(product_model)

        self.stdout.write(self.style.SUCCESS(SUCCESS_MESSAGE))
