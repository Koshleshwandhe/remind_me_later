from django.urls import path
from django.http import JsonResponse
from reminders.views import create_reminder

def index(request):
    return JsonResponse({'message': 'Welcome to Remind Me Later API!'})

urlpatterns = [
    path('', index),
    path('api/create_reminder/', create_reminder, name='create_reminder'),
]
