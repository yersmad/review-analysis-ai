from django.urls import path
from . import views


app_name = "review_analysis_ai"

urlpatterns = [
    path("analysis/", views.AnalysisListView.as_view(), name="analysis_list"),
    path("reviews/", views.ReviewListCreateView.as_view(), name="review_list"),
    path("analysis/<int:pk>/", views.AnalysisDetailView.as_view(), name="analysis_detail"),
    path("reviews/<int:pk>/", views.ReviewDetailView.as_view(), name="review_detail"),
    path("reviews/create/", views.PromptView.as_view(), name="prompt"),

]
