from django.db import models


class Fruit(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

