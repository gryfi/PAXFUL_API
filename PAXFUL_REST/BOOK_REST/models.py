from django.db import models

"""
# Author and   Book  Models
"""

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True)
