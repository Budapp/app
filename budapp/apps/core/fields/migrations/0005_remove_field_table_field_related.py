# Generated by Django 3.1.7 on 2021-03-30 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0004_auto_20210330_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='field',
            name='table_field_related',
        ),
    ]
