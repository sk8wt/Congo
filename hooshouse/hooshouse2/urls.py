"""hooshouse URL Configuration

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
from dbviewer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apt_building/', views.test, name="apt_building"),
    path('create_apt/', views.create_apt, name="create_apt"),
    path('delete_apt/<apt_name>', views.delete_apt, name="delete_apt"),
    path('landlords/', views.view_landlords, name = "view_landlords"),
    path('landlords/delete/<comp_name>', views.delete_landlord, name = 'delete_landlord'),
    path('view_units/', views.view_units, name="view_units"),
    path('units/delete/<unit_add>/<apt_num>', views.delete_unit, name = "delete_unit"),
    path('units/update/<unit_add>/<apt_num>', views.update_unit, name = "update_unit"),
    path('view_leases/', views.view_leases, name = "view_leases"),
    path('lease/delete/<cid>', views.delete_lease, name = "delete_lease"),
    path('units/lease/<unit_add>/<apt_num>', views.lease_unit, name = "lease_unit"),
    path('create_tenant/', views.create_tenant, name = "create_tenant"),
    path('tenant/', views.tenants, name="tenant"),
    path('tenant/delete/<cid>', views.delete_tenants, name = "delete_tenants"),
    path('available_apt/', views.get_num_available, name = 'get_num_available'),
    path('tenant/update/<cid>', views.update_tenants, name = "update_tenants"),
    path('maintains/', views.view_maintains, name = "view_maintains"),
    path('maintains/delete/<apt_addr>', views.delete_maintains, name = 'delete_landlord'),
    path('maintains/update/<apt_addr>', views.update_maintains, name = "update_maintains"),
]
