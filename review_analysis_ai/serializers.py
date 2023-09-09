from rest_framework import serializers

from .models import Review, Analysis

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'

class PromptRequestSerializer(serializers.Serializer):
    url_reviews = serializers.CharField(max_length=512)
