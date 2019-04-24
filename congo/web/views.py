from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


from classes import db_queries


def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")
