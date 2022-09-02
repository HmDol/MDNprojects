from django.urls import path, include

from htmlapp.views import hello

urlpatterns = [
    path('', hello, name = 'hello')
]