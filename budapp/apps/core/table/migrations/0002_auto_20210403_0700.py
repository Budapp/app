# Generated by Django 3.1.7 on 2021-04-03 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Name'),
        ),
    ]
