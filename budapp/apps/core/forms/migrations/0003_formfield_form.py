# Generated by Django 3.1.7 on 2021-03-30 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20210330_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='form',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forms.form'),
            preserve_default=False,
        ),
    ]