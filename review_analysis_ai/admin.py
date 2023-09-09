from django.contrib import admin
from .models import Review, Analysis

# Register your models here.
class AdminReview(admin.ModelAdmin):
    fields = ["content", "url", "author"]

class AdminAnalysis(admin.ModelAdmin):
    fields = ["response", "opinion","reviews"]
 

admin.site.register(Analysis, AdminAnalysis)
admin.site.register(Review, AdminReview)