from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    is_super = models.BooleanField(default=False)
    email = models.EmailField(max_length=250, null=True)


class Book(models.Model):
    name = models.CharField(max_length=10)
    rate = models.IntegerField(default=0)
    author = models.ManyToManyField(Person, related_name='books')


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(Person, on_delete=models.SET('user_deleted'), related_name='comments')
    create_date = models.DateTimeField(auto_now_add=True)
