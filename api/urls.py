from django.urls import path
from .views import api_status, receive_data, send_basic_sheet

urlpatterns = [
    path('', api_status, name='api_base'),
    path('status/', api_status, name='api_status'),
    path('data/', receive_data, name='receive_data'),
    path('send/', send_basic_sheet, name='send_basic_sheet'),
]