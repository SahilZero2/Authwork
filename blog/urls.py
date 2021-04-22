from django.urls import path
from .views import blog,blogpost
urlpatterns = [
    path('', blog , name='blog'),
    

]