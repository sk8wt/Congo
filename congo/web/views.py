from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


from classes import db_queries


def test(request):
    data = db_queries.list_merch()
    return render(request,"homepage.html",{'data':data})
