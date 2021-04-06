from django.urls import path
from company import views

urlpatterns = [
    path(
        route='mdfy_usr/<company_id>', 
        view=views.modify_user, 
        name='user_detail'
    ),
    path(
        route='position/<company_id>', 
        view=views.modify_position, 
        name='position_detail'
    ),
    path(
        route='rslts/<company_id>', 
        view=views.test_results_list, 
        name='test_results_list'
    ),

]