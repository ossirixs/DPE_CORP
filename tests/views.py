from django.shortcuts import render
from tests.models import CIE_form


def test_selector(request):

    title = 'Prueba psicométrica'
    result = 0

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CIE_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            q_1 = int(form.cleaned_data['q_1'])
            q_2 = int(form.cleaned_data['q_2'])
            q_3 = int(form.cleaned_data['q_3'])

            sum = q_1 + q_2 + q_3

            result = 'Tu resultado fue: %d' % sum

        # if a GET (or any other method) we'll create a blank form
    else:
        form = CIE_form()

    return render(request, 'test_base.html', dict(title=title,
                                                  result=result,
                                                  form=form))
