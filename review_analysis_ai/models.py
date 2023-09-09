from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} - {self.created_at}"

class Analysis(models.Model):
    reviews = models.OneToOneField(Review, on_delete=models.CASCADE)
    response = models.TextField()
    opinion = models.TextField(max_length=10)
    analysis_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for Review by {self.review.user.username} - {self.analysis_date}"