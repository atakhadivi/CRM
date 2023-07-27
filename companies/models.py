# models.py

from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Company(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  
  def __str__(self):
    return self.name