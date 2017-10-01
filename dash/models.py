# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    def __str__(self):
        return "(%s, %s)" % (self.uname, self.pwd)

class Session(models.Model):
    uname = models.ForeignKey('User', on_delete=models.CASCADE)
    skey = models.CharField(max_length=128)
    def __str__(self):
        return "(%s, %s)" % (self.uname, self.skey)

class Team(models.Model):
    uname = models.ForeignKey('User', on_delete=models.CASCADE)
    city = models.CharField(max_length=60)
    tname = models.CharField(max_length=40)
    def __str__(self):
        return "(%s, %s, %s)" % (self.uname, self.city, self.tname)
