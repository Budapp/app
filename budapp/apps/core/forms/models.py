from django.db import models

"""
Form structure
|----------------|
| Form           |
|----------------|
|   Form steps   |
|----------------|
|    Form fields |
|----------------|
|         Field  |
|----------------|
"""


class Form (models.Model):
    name = models.CharField(u'Name', max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'

    def __str__(self):
        return self.name


class FormStep(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    
    name = models.CharField(u'Name', max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Form Step'
        verbose_name_plural = 'Form Steps'

    def __str__(self):
        return self.name

class FormField(models.Model):
    form_step = models.ForeignKey(FormStep, on_delete=models.CASCADE)
    field = models.ForeignKey('fields.Field', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Form field'
        verbose_name_plural = 'Form fields'

    def __str__(self):
        return f'{self.field} - {self.form_step}'
