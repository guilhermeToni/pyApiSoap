from django.urls import path
from .views import api_status, receive_data

urlpatterns = [
    path('status/', api_status, name='api_status'),
    path('data/', receive_data, name='receive_data'),
]