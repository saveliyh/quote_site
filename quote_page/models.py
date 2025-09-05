from django.db import models


class Quote(models.Model):
    quote = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    views = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    weight = models.IntegerField()
