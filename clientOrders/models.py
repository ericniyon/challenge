from django.db import models
from django.contrib.auth.models import User


class ClientOrders(models.Model):
    orderName = models.CharField(max_length=100)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.orderName
