"""dpe_app URL Configuration"""
#Django
from django.contrib import admin
from django.urls import path, include
#App
from dpe_app import views as dpe_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('users/',include(('users.urls','users'), namespace='users')),
    path(
        route='dsh', 
        view=dpe_views.dashboard, 
        name='dashboard'
    ),
    path(
        route='cmp', 
        view=dpe_views.company_list, 
        name='companies'
    ),
    path(
        route='cmp/dtl/<company_name>/', 
        view=dpe_views.company_detail, 
        name='company_detail'
    ),
    path(
        route='pstn', 
        view=dpe_views.position_list, 
        name='positions'
    ),
]
