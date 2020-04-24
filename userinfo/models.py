from django.db import models


# Create your models here.

class Submission(models.Model):
    prob_level = models.CharField(max_length=1)
    prob_rating = models.IntegerField()
    prob_tags = models.BooleanField(default=False)
