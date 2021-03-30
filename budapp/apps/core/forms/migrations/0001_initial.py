# Generated by Django 3.1.7 on 2021-03-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fields', '0005_remove_field_table_field_related'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True)),
                ('fields', models.ManyToManyField(to='fields.Field')),
            ],
            options={
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
            },
        ),
    ]