from django.db import models

class Drink(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=1500)

  def __str__(self):
    return self.name