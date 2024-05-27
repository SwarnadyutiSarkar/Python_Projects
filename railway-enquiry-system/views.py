import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view

API_URL = "https://api.railwayapi.com/v2/"  # Replace with actual API URL
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key

@api_view(['GET'])
def train_status(request, train_number):
    response = requests.get(f"{API_URL}live/train/{train_number}/date/20210527/apikey/{API_KEY}/")
    return JsonResponse(response.json())

@api_view(['GET'])
def train_schedule(request, train_number):
    response = requests.get(f"{API_URL}schedule/train/{train_number}/apikey/{API_KEY}/")
    return JsonResponse(response.json())

@api_view(['GET'])
def train_route(request, train_number):
    response = requests.get(f"{API_URL}route/train/{train_number}/apikey/{API_KEY}/")
    return JsonResponse(response.json())
