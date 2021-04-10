from django.db import models


class Table(models.Model):
    name = models.CharField(u'Name', max_length=50, unique=True)
    description = models.TextField(u'Description')

    def __str__(self):
        return self.name


class Document(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)


class DocumentFieldValue(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE)

    field = models.ForeignKey('fields.Field', on_delete=models.CASCADE)
    value = models.CharField('Field value', max_length=1000)
