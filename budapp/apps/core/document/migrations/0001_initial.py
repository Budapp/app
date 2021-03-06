# Generated by Django 3.1.7 on 2021-04-10 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('table', '0003_document_documentfieldvalue'),
        ('fields', '0002_auto_20210403_0700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field', to='fields.field')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='table.table')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
    ]
