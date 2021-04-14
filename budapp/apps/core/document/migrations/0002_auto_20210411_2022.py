# Generated by Django 3.1.7 on 2021-04-11 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0002_auto_20210403_0700'),
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='field',
        ),
        migrations.RemoveField(
            model_name='document',
            name='value',
        ),
        migrations.CreateModel(
            name='DocumentValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(blank=True, null=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.document')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field', to='fields.field')),
            ],
            options={
                'verbose_name': 'Document value',
                'verbose_name_plural': 'Document values',
            },
        ),
    ]
