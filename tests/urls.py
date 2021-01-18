from django.urls import path
from . import views
from tests.views import FormWizardView
from tests.forms import CIE_form_1, CIE_form_2


urlpatterns = [
    path(
        route='',
        view=views.test_selector,
        name='test_selector'
    ),
    path(
        route='CIE',
        view=FormWizardView.as_view(),
        name='cie_test'
    ),

]
