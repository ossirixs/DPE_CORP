from django.shortcuts import render
from tests.models import CIE_form


def test_selector(request):

    title = 'Cuestionario CIE'
    result = 0
    sum = 0
    true = 0
    false = 0
    est = 0
    ans = 0

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
            q_4 = int(form.cleaned_data['q_4'])
            q_5 = int(form.cleaned_data['q_5'])
            q_6 = int(form.cleaned_data['q_6'])
            q_7 = int(form.cleaned_data['q_7'])
            q_8 = int(form.cleaned_data['q_8'])
            q_9 = int(form.cleaned_data['q_9'])
            q_10 = int(form.cleaned_data['q_10'])
            q_11 = int(form.cleaned_data['q_11'])
            q_12 = int(form.cleaned_data['q_12'])
            q_13 = int(form.cleaned_data['q_13'])
            q_14 = int(form.cleaned_data['q_14'])
            q_15 = int(form.cleaned_data['q_15'])
            q_16 = int(form.cleaned_data['q_16'])
            q_17 = int(form.cleaned_data['q_17'])
            q_18 = int(form.cleaned_data['q_18'])
            q_19 = int(form.cleaned_data['q_19'])
            q_20 = int(form.cleaned_data['q_20'])

            sum = (q_1 + q_2 + q_3 + q_4 + q_5 + q_6 + q_7 + q_8 + q_9 + q_10 + q_11 + q_12 + q_13 + q_14 + q_15 + q_16
                   + q_17 + q_18 + q_19 + q_20)

            print(sum)

            est = q_1 + q_8 + q_18
            ans = q_2 + q_19

            if est < 15:
                result = "Est (Estabilidad Emocional) Medio: Se trata de un individuo con control y estabilidad emocionales."
            else:
                result = "Est (Estabilidad Emocional) Bajo: Impulsiva, nerviosa e irritable, esta persona se sobreexcita " \
                         "ante las circunstancias que no puede controlar. Es susceptible e irritable emocionalmente. " \
                         "Se altera fácilmente. Manifiesta cambios de ánimo y mal humor."

        # if a GET (or any other method) we'll create a blank form
    else:
        form = CIE_form()

    return render(request, 'test_base.html', dict(title=title,
                                                  result=result,
                                                  true=sum,
                                                  false=20-sum,
                                                  est=est,
                                                  ans=ans,
                                                  form=form))
