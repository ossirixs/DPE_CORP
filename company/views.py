#Django.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models import Q

#Models.
from company.models import Company, TestCode
from users.models import User

#Forms
from company.forms import NewCompanyForm
from users.forms import SignUpForm
from users.models import User

@login_required
@never_cache
def company_list(request):
    """ List all available companies."""
    print("company_list")
    
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
            # Get allcomapnies.
            companies = Company.objects.all()
            main_companies = Company.objects.filter(company_type='MAIN')
            company_form = NewCompanyForm(request.POST)
            if company_form.is_valid():
                print('valid form')
                new_company = company_form.save()
                

            return render(request,'company/companies.html', {
                                                                'companies':companies,
                                                                'saved_company':'True',
                                                                'new_company':new_company,
                                                                'main_companies':main_companies,
                                                                'user': request.user
                                                            })
    elif request.method == 'GET':
        # Get user.
        user = request.user

        if user.type == User.Types.CLIENT_MAIN:
            # Get main companie and also companies that belongs to the client 
            companies = Company.objects.filter(Q(id=user.company) | Q(company_main=user.company))
        elif user.type == User.Types.CLIENT_MAIN:
            # If a sub client, get only it's own company
            companies = Company.objects.filter(id=user.company)
        elif user.type == User.Types.ADMIN_DPE:
            # Get main companies.
            companies = Company.objects.all()


        return render(request,'company/companies.html', {
                                                            'companies':companies,
                                                            'saved_company':'False',
                                                            'companies':companies,
                                                            'user': request.user
                                                        })

@login_required
def company_detail(request,company_id):
    """ Company detail and actions."""

    user = request.user
    

    if user.type == User.Types.CLIENT_MAIN:
        # Get selected company and all sub companies data.
        companies = Company.objects.filter(Q(id=user.company) | Q(company_main=user.company))
        # Get company and codes data.
        selected_company = Company.objects.get(id=company_id)
        #If company main = 0, then this is a MAIN company
        if selected_company.company_main == 0:
            # Get all users from Main and sub companies.
            company_users = User.objects.filter(Q(company=company_id) | Q(company_main=company_id))
            # Set the company main id to false since this is a Main company
            company_main = False
            # Get all codes from this Main company and its sub companies.
            company_codes = TestCode.objects.filter(company__in=companies)
        #Else, this is a sub company
        else:
            # Get just users from this sub company.
            company_users = User.objects.filter(Q(company=company_id))
            # Get the main company data for this sub company.
            company_main = Company.objects.get(id=selected_company.company_main)
            # Get codes for just this company.
            company_codes = TestCode.objects.filter(company=selected_company)

    elif user.type == User.Types.CLIENT:
        # If a sub client, get only it's own company.
        companies = Company.objects.filter(id=user.company)
        # Get company and codes data.
        selected_company = Company.objects.get(id=company_id)
        # Get just users from this sub company.
        company_users = User.objects.filter(Q(company=company_id))
        # Get the main company data for this sub company.
        company_main = Company.objects.get(id=selected_company.company_main)
        # Get codes for just this company.
        company_codes = TestCode.objects.filter(company=selected_company)

    elif user.type == User.Types.ADMIN_DPE:
        # Get company and codes data.
        selected_company = Company.objects.get(id=company_id)
        # If selected company is a main company, get its data
        companies = Company.objects.filter(Q(id=selected_company.id) | Q(company_main=selected_company.id))
        # Get just users from this sub company.
        company_users = User.objects.filter(Q(company=selected_company.id) | Q(company_main=selected_company.id))
        # Set the company main id to false since this is an admin dpe user.
        company_main = False
        # Get all codes from this Main company and its sub companies.
        company_codes = TestCode.objects.filter(company__in=companies)

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
        elif request.POST.get('create_code'):
            print('create code')
            company = Company.objects.get(id=request.POST.get('company_id'))

            test = request.POST.get('test')
            code = test+"CODE"+"-"+company.company_name
            expiration = request.POST.get('expiration')
            
            new_code = TestCode(user=request.user,company=company,test=test,code=code,expiration=expiration)
            new_code.save()
            print("creating")
            
    return render(request,'company/company_detail.html', {
                                                            "company":selected_company,
                                                            "company_main":company_main,
                                                            "company_users":company_users,
                                                            "companies": companies,
                                                            "company_codes":company_codes,
                                                            'user': user
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
                # "user":company_user,
                "company_name":company_name,
                'user': request.user
            }

            return render(request, "company/user_detail.html", args)
