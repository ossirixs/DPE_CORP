from django.urls import path
from . import views
from tests.views import CIE, test_result
from tests.forms import CIE_form_1, CIE_form_2


urlpatterns = [
    path(
        route='cie/<test_code>',
        view=CIE.as_view(),
        name='cie_test'
    ),
    path(
        route='cie_instructions/<test_code>',
        view=views.cie_instructions,
        name='cie_instructions'
    ),
    path(
        route='cpecon/<test_code>',
        view=CIE.as_view(),
        name='dpecon_test'
    ),
    path(
        route='results/<test_type>/<test_id>',
        view=views.test_result,
        name='test_result'
    ),
]
