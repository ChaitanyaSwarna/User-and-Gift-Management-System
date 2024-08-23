from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class gift(models.Model):
    giftname = models.CharField(max_length=20)
    id_1 = models.IntegerField()