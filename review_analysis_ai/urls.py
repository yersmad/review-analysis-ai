from django.urls import path
from . import views


app_name = "review_analysis_ai"

urlpatterns = [
    path("", views.index, name="index"),
]
