from django.urls import path
from users import views

urlpatterns = [
    path(
        route='',
        view=views.login_view, 
        name='login'
    ),
    path(
        route='admn',
        view=views.users_adm,
        name='users_admn'
    ),
    path(
        route='logout',
        view=views.log_out, 
        name='logout'
    ),
]
