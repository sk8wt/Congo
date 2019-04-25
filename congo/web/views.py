from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


# Create your views here.


from classes import db_queries


def test(request):
    data = db_queries.list_merch()
    return render(request,"homepage.html",{'data':data})

def login(request):
    if request.method == "GET":
        form = login_form()
    else:
        form = login_form(request.POST)
        data = []
        if form.is_valid():
            #data = db_queries.login(str(form.cleaned_data['Username']))
            return redirect('profile',name=form.cleaned_data['Username'])
    return render(request,"login.html", {'form':form})

def profile(request, name):
    if request.method == "POST":
        n = request.POST['Itemname']
        price = int(request.POST['price'])
        desc = request.POST['Itemdesc']
        id = db_queries.get_id(name)
        db_queries.create_merch(request,n, price, desc, 0,'',name, id)
    data = db_queries.login(name)
    return render(request,"profilepage.html", {'data':data,'name':name})

def create_new_merch(request, name):
    return render(request,"saveitem.html", {'name':name})
def delete_merch(request, name, id):
    db_queries.delete_merch(request,id)
    return redirect('profile',name=name)
def delete_merch(request, name, id):
    db_queries.delete_merch(request,id)
    return redirect('profile',name=name)

def update_merch(request, name, id):
    return redirect('profile',name=name)
