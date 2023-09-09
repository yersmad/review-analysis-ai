from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect, HttpResponse

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

import os, openai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .models import Review, Analysis
from .serializers import ReviewSerializer, AnalysisSerializer, PromptRequestSerializer

api_key = os.getenv("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", None)


def get_reviews(request, url):
    driver = webdriver.Chrome()
    driver.get(url)
    try:
        driver.implicitly_wait(4)
        reviews = driver.find_elements(By.CLASS_NAME, "feedback__text")

        review_texts = list(map(lambda x: x.text, reviews))
        
        return review_texts
    except:
        return HttpResponse("Error\n")
    finally:
        driver.quit()


class AnalysisListView(generics.ListAPIView):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer

class AnalysisDetailView(generics.RetrieveDestroyAPIView):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer

class ReviewDetailView(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
 
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

class PromptView(APIView):    
    def post(request, url):
        reviews = get_reviews(request, url)
        prompt_serializer = PromptRequestSerializer(url_reviews=reviews)
        if prompt_serializer.is_valid():
            prompt = prompt_serializer.validated_data['content']
            api_key = os.environ.get('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')
            endpoint = 'https://api.openai.com/v1/chat/completions'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {"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"}'
                }
            data = {
                'messages': [{'role': 'system', 'content': 'You are a helpful assistant that provides information.'},
                             {'role': 'user', 'content': f'Проведи общий анализ данных отзывов стоит брать данный товар или нет: {reviews} и дай оценку по критериям: позитивный, негативный, нейтральный.'}],
            }
            response = requests.post(endpoint, json=data, headers=headers)
            if response.status_code == 200:

                return Response({'response': response.json()['choices'][0]['message']['content']})
            else:
                return Response({'error': 'Failed to process request'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
