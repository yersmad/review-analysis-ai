from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

class Analysis(models.Model):
    reviews = models.OneToOneField(Review, on_delete=models.CASCADE)
    responses = models.TextField()
    opinion = models.TextField(max_length=10)
    analysis_date = models.DateTimeField(auto_now_add=True)