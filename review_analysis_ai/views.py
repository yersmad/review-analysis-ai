from django.shortcuts import render

from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def index(request):
    return Response(request, status=200)
