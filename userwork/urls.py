from django.urls import path
from .views import createaccount

urlpatterns = [
    path('', createaccount, name='createaccount'),
    
]