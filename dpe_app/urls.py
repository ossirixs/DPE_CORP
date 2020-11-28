"""dpe_app URL Configuration"""
#Django.
from django.contrib import admin
from django.urls import path, include
#Apps.
from dpe_app import views as dpe_views
from company import views as company_views
from company import views as company_views
from tests import views as tests_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('users/', include(('users.urls','users'), namespace='users')),
    path('tests/', include('tests.urls')),
    path(
        route='dsh', 
        view=dpe_views.dashboard, 
        name='dashboard'
    ),
    path(
        route='cmp', 
        view=company_views.company_list, 
        name='companies'
    ),
    path(
        route='cmp/dtl/<company_name>/', 
        view=company_views.company_detail, 
        name='company_detail'
    ),
    path(
        route='pstn',
        view=dpe_views.position_list,
        name='positions'
    ),
]
