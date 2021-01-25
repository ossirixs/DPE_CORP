from django.urls import path
from . import views
from tests.views import CIE
from tests.forms import CIE_form_1, CIE_form_2


urlpatterns = [
    path(
        route='',
        view=views.test_selector,
        name='test_selector'
    ),
    path(
        route='cie/<test_code>',
        view=CIE.as_view(),
        name='cie_test'
    ),
    path(
        route='cpecon/<test_code>',
        view=CIE.as_view(),
        name='dpecon_test'
    ),
]
