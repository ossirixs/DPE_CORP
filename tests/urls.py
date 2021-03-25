from django.urls import path
from . import views
from tests.views import CIE, test_result
from tests.forms import CIE_form_1, CIE_form_2


urlpatterns = [
    path(
        route='cie_instructions/<test_code>',
        view=views.cie_instructions,
        name='cie_instructions'
    ),
    path(
        route='cie/<test_code>',
        view=CIE.as_view(),
        name='cie_test'
    ),
    path(
        route='results/<test_type>/<test_id>',
        view=views.test_result,
        name='test_result'
    ),
    path(
        route='integrity_instructions/<test_code>',
        view=views.integrity_instructions,
        name='integrity_instructions'
    ),
    path(
        route='integrity/<test_code>',
        view=views.integrity_test,
        name='integrity_test'
    ),
    path(
        route='integrity_results/<test_type>/<test_id>',
        view=views.integrity_test_result,
        name='integrity_test_result'
    ),
    path(
        route='max_instructions/<test_code>',
        view=views.max_instructions,
        name='max_instructions'
    ),
    path(
        route='max/<test_code>',
        view=views.max_test,
        name='max_test'
    ),
        path(
            route='max_results/<test_type>/<test_id>',
            view=views.max_test_result,
            name='max_test_result'
        ),
]
