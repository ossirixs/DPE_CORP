from django.shortcuts import render
from tests.models import ObjectCIE
from company.models import TestCode
from tests.forms import CIE_form_1, CIE_form_2, candidato
from formtools.wizard.views import SessionWizardView
from django.shortcuts import get_object_or_404
from tests.utils import clean_data


class CIE(SessionWizardView):
    form_list = [candidato, CIE_form_1, CIE_form_2]

    def get_template_names(self):
        return 'test.html'

    def done(self, form_list, **kwargs):
        code = kwargs['test_code']
        test_code = TestCode.objects.get(code=code)
        cuestionario = ObjectCIE()

        for form in form_list:
            form_data = form.cleaned_data
            for key, value in form_data.items():
                setattr(cuestionario, key, value)
                # print(key, value)
        cuestionario.codigo = test_code
        cuestionario.save()
        title = 'ACIES'
        return render(self.request, 'finish.html', dict(form_data = [form.cleaned_data for form in form_list],
                                                        title = title))
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
        form = CIE_form_1(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            cuestionario = ObjectCIE(
                q_1=int(form.cleaned_data['q_1']),
                q_2=int(form.cleaned_data['q_2']),
                q_3=int(form.cleaned_data['q_3']),
                q_4=int(form.cleaned_data['q_4']),
                q_5=int(form.cleaned_data['q_5']),
                q_6=int(form.cleaned_data['q_6']),
                q_7=int(form.cleaned_data['q_7']),
                q_8=int(form.cleaned_data['q_8']),
                q_9=int(form.cleaned_data['q_9']),
                q_10=int(form.cleaned_data['q_10']),
                q_11=int(form.cleaned_data['q_11']),
                q_12=int(form.cleaned_data['q_12']),
                q_13=int(form.cleaned_data['q_13']),
                q_14=int(form.cleaned_data['q_14']),
                q_15=int(form.cleaned_data['q_15']),
                q_16=int(form.cleaned_data['q_16']),
                q_17=int(form.cleaned_data['q_17']),
                q_18=int(form.cleaned_data['q_18']),
                q_19=int(form.cleaned_data['q_19']),
                q_20=int(form.cleaned_data['q_20']),
            )
            cuestionario.save()

            sum = 20

            print(sum)

            est = 5
            ans = 15

            if est < 15:
                result = "Est (Estabilidad Emocional) Medio: Se trata de un individuo con control y estabilidad emocionales."
            else:
                result = "Est (Estabilidad Emocional) Bajo: Impulsiva, nerviosa e irritable, esta persona se sobreexcita " \
                         "ante las circunstancias que no puede controlar. Es susceptible e irritable emocionalmente. " \
                         "Se altera fácilmente. Manifiesta cambios de ánimo y mal humor."


        # if a GET (or any other method) we'll create a blank form
    else:
        form = CIE_form_1()

    cuestionarios = ObjectCIE.objects.all()
    for cuestionario in cuestionarios:
        print(cuestionario, cuestionario.id, cuestionario.q_1, cuestionario.q_2)

    return render(request, 'test_base.html', dict(title=title,
                                                  result=result,
                                                  true=sum,
                                                  false=20-sum,
                                                  est=est,
                                                  ans=ans,
                                                  form=form))

def test_result(request, test_type, test_id):

    cuestionario = get_object_or_404(ObjectCIE, pk=test_id)

    try:
        q_1 = cuestionario.q_1
        q_2 = cuestionario.q_2
        q_3 = cuestionario.q_3
        q_4 = cuestionario.q_4
        q_5 = cuestionario.q_5
        q_6 = cuestionario.q_1
        q_7 = cuestionario.q_2
        q_8 = cuestionario.q_3
        q_9 = cuestionario.q_4
        q_10 = cuestionario.q_5
        q_40 = cuestionario.q_40
        q_41 = cuestionario.q_41
    except:
        pass

    EST_true = [q_2, q_3, q_40]
    EST_false = [q_1, q_8, q_41]

    EST = 0
    for pregunta in EST_true:
        EST += clean_data(pregunta, invert=0)
    for pregunta in EST_false:
        EST += clean_data(pregunta, invert=1)
    print('est perra', EST)

    title = 'PLOX'

    return render(request, 'test_result.html', dict(title=title))
