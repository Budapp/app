# Generated by Django 3.1.7 on 2021-03-30 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0005_remove_field_table_field_related'),
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='fields',
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fields.field')),
            ],
            options={
                'verbose_name': 'Form field',
                'verbose_name_plural': 'Form fields',
            },
        ),
    ]
