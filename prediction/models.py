from unicodedata import name
from django.db import models
from account.models import Client

# Create your models here.


class PredictionModel(models.Model):
    name = models.CharField(max_length=100)
    pickle_file = models.FileField()

    def __str__(self):
        return self.name


class Prediction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pred_model = models.ForeignKey(PredictionModel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.client.username
