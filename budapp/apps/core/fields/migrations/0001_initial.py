# Generated by Django 3.1.7 on 2021-04-02 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('required', models.BooleanField(default=False, verbose_name='Required')),
                ('unique', models.BooleanField(default=False, verbose_name='Unique')),
                ('element', models.CharField(blank=True, choices=[('input', 'Input'), ('foreign_key', 'Relation field (1 - 1)'), ('many_to_many', 'Relation field (1 - N)')], default='input', max_length=20, null=True, verbose_name='Element')),
                ('input_type', models.CharField(blank=True, choices=[('text', 'Text'), ('url', 'Url'), ('email', 'Email')], default='text', max_length=20, null=True, verbose_name='Type')),
                ('table_relation_type', models.CharField(blank=True, choices=[('foreign_key', 'Foreign key'), ('many_to_many', 'Many to many')], default='foreign_key', max_length=20, null=True, verbose_name='Table relation type')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='table.table')),
                ('table_related', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='table_related', to='table.table')),
            ],
        ),
    ]
