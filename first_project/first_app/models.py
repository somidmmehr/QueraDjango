from django.contrib.auth.models import User
from django.db import models
from django.db.models import *
from django.core.validators import *


class PersonManager(models.Manager):
    def __init__(self):
        self._db = 'MySQL'
        self._hints = None
        self.name = None
        super().db_manager(self._db)

    def latest_logins(self, count=10):
        return self.order_by('-last_login')[:count]

    def similar_name_username(self):
        return self.filter(name=F('username'))


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=150, validators=[MinLengthValidator(6)])
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=64, validators=[MinLengthValidator(6)])
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    is_super = models.BooleanField(default=False)
    email = models.EmailField(max_length=250, null=True, blank=True)

    objects = models.Manager()
    people = PersonManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}" \



class Book(models.Model):
    name = models.CharField(max_length=10)
    rate = models.IntegerField(default=0)
    author = models.ManyToManyField(Person, related_name='books')

    def __str__(self):
        authors = " - ".join([x.first_name+" "+x.last_name for x in self.author.all()])
        return f"{self.name} , rate: {self.rate}, author: {authors}"


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(Person, on_delete=models.SET('user_deleted'), related_name='comments')
    create_date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    COUNTRY_CHOICES = [
        ('IR', 'Iran'),
        ('JP', 'Japan'),
        ('TU', 'Turkey'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20, null=True, blank=True, choices=COUNTRY_CHOICES)

