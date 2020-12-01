#Django.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models import Q

#Models.
from company.models import Company
from users.models import User

#Forms
from company.forms import NewCompanyForm
from users.forms import SignUpForm

@login_required
@never_cache
def company_list(request):
    """ List all available companies."""
    print("listing")
    companies = Company.objects.all()
    if request.method == 'POST':
        action = request.POST.get('action','')
        #Company selected.
        if action == "select":
            company = request.POST['company']
            if company != "" and company != 0:
                return redirect('company_detail' , company_id=company)
        #Create a company.
        elif action == "create":
            print('create')
            company_form = NewCompanyForm(request.POST)
            if company_form.is_valid():
                print('valid form')
                new_company = company_form.save()
                

            return render(request,'company/companies.html', {
                                                                'companies':companies,
                                                                'saved_company':'True',
                                                                'new_company':new_company,
                                                            })
    return render(request,'company/companies.html', {
                                                        'companies':companies,
                                                        'saved_company':'False',
                                                    })

@login_required
def company_detail(request,company_id):
    """ Company detail and actions."""

    selected_company = Company.objects.get(id=company_id)
    #If company main = 0, then this is a MAIN company
    if selected_company.company_main == 0:
        company_users = User.objects.filter(Q(company=company_id) | Q(company_main=company_id))
    #Else, this is a sub company
    else:
        company_users = User.objects.filter(Q(company=company_id))
    print("             company_users",company_users)
    # If is a sub company, retrieve main company data
    if selected_company.company_main > 0:
        company_main = Company.objects.get(id=selected_company.company_main)
    else:
        company_main = False

    if request.method == 'POST':
        if request.POST.get('update'):
            print('update', selected_company)
            selected_company.company_name = request.POST.get('company_name')
            selected_company.company_contact = request.POST.get('company_contact')
            selected_company.company_email = request.POST.get('company_email')
            selected_company.save()
        elif request.POST.get('create_user'):
            print('create_user')
            form = SignUpForm(request.POST)
            print('form.errors()',form.errors)
            if form.is_valid():
                print('company main', form.cleaned_data['company_main'])
                form.save()

    return render(request,'company/company_detail.html', {
                                                            "company":selected_company,
                                                            "company_main":company_main,
                                                            "company_users":company_users,
                                                            })

@login_required
def modify_user(request, company_name):
    """Modify a company user."""
    if request.method == 'POST':
        #Select an user.
        if request.POST.get('company_user_id'):
            user_id = request.POST.get('company_user_id')
            selected_user = User.objects.get(id=user_id)
            print("selectd user", selected_user.first_name)

            args = {
                "user":selected_user,
                "company_name":company_name,
            }

            return render(request, "company/user_detail.html", args)
        #Update user.
        elif request.POST.get('update_user'):
            user_id = request.POST.get('user_id')
            company_user = User.objects.get(id=user_id)
            print("selectd user to update >>>>> ", company_user.first_name)

            company_user.username = request.POST.get('username')
            company_user.first_name = request.POST.get('first_name')
            company_user.last_name = request.POST.get('last_name')
            company_user.second_last_name = request.POST.get('second_last_name')
            company_user.email = request.POST.get('email')
            company_user.save()
            args = {
                "user":company_user,
                "company_name":company_name,
            }

            return render(request, "company/user_detail.html", args)
