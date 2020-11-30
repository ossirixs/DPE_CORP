from django.urls import path
from company import views

urlpatterns = [
    path(
        route='clt_usr/<company_name>', 
        view=views.modify_user, 
        name='user_detail'
    ),

]