from django.urls import path
from . import views


urlpatterns = [
    path(
        route='',
        view=views.test_selector,
        name='test_selector'
    ),
]
