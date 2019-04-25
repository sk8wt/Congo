"""congo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', views.test, name="test"),
    path('login/', views.login, name="login"),
    path('profile/<name>/',views.profile,name="profile"),
    path('profile/<name>/newitem/',views.create_new_merch,name="newMerch"),
    path('profile/<name>/deleteitem/<id>/',views.delete_merch,name="delMerch"),
    path('profile/<name>/updateitem/<id>/',views.update_merch,name="uptMerch"),
    path(r'^', views.login, name="login"),
    path("", views.login, name="login"),
    path(r'^.*', views.login, name="login"),
]
