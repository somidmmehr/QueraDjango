from django.db import models


class BookManager(models.Manager):
    def __init__(self):
        self._db = "MySQL"
        self._hints = None
        self.name = None
        super().db_manager(self._db)


# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    objects = BookManager()
