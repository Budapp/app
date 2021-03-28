from django.db import models


class Table(models.Model):
    name = models.CharField(u'Name', max_length=50)
    description = models.TextField(u'Description')

    def __str__(self):
        return self.name
