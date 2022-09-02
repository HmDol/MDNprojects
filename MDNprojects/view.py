from django.http import HttpResponse
from django.shortcuts import render


def MDN_home(request):
    return render(request, "MDN_home.html")