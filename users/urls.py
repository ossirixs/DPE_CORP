from django.urls import path
from users import views

urlpatterns = [
    path(
        route='', 
        view=views.login_view, 
        name='login'
    ),
    path(
        route='/dsh', 
        view=views.dashboard, 
        name='dashboard'
    ),

]
