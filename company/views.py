#Django.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models import Q
from datetime import datetime

#Models.
from company.models import Company, TestCode, CompanyTest, TestCatalog
from users.models import User
from tests.models import ObjectCIE

#Forms
from company.forms import NewCompanyForm, TestCodeForm, CompanyTestForm
from users.forms import SignUpForm
from users.models import User

@login_required
@never_cache
def company_list(request):
    """ List all available companies."""
    print("company_list")
    companies = ''
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
            companies = Company.objects.all().order_by('modified')
            main_companies = Company.objects.filter(company_type='MAIN')
            if request.POST.get('company_type') == 'MAIN':
                company_form = NewCompanyForm({'company_type':request.POST.get('company_type'),
                                                'company_name':request.POST.get('company_name'),
                                                'company_contact':request.POST.get('company_contact'),
                                                'company_phone':request.POST.get('company_phone'),
                                                'company_email':request.POST.get('company_email')})
            else:
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

        # Get main company and also companies that belongs to the client 
        if user.type == User.Types.CLIENT_MAIN:
            companies = Company.objects.filter(Q(id=user.company.id) | Q(company_main=user.company.id)).order_by('modified')
        # If a sub client, get only it's own company
        elif user.type == User.Types.CLIENT:
            companies = Company.objects.filter(id=user.company.id).order_by('modified')
        # Get main companies.
        elif user.type == User.Types.ADMIN_DPE:
            companies = Company.objects.all().order_by('modified')


        return render(request,'company/companies.html', {
                                                            'companies':companies,
                                                            'saved_company':'False',
                                                            'main_companies':companies.filter(company_type='MAIN'),
                                                            'user': request.user
                                                        })

@login_required
@never_cache
def company_detail(request,company_id):
    """ Company detail and actions."""

    user = request.user
    
    # Get each companies details according to the user type
    if user.type == User.Types.CLIENT_MAIN:
        # Get selected company and all sub companies data.
        companies = Company.objects.filter(Q(id=user.company.id) | Q(company_main=user.company.id))
        # Get company and codes data.
        selected_company = Company.objects.get(id=company_id)
        #If company main, then this is a MAIN company
        if selected_company.company_main:
            # Get all users from Main and sub companies.
            company_users = User.objects.filter(Q(company=company_id) | Q(company_main=company_id))
            # Set the company main id to false since this is a Main company
            company_main = False
            # Get all codes from this company.
            #company_codes = TestCode.objects.filter(company__in=companies)
            company_codes = TestCode.objects.filter(company=selected_company)
        #Else, this is a sub company
        else:
            # Get just users from this sub company.
            company_users = User.objects.filter(Q(company=company_id))
            # Get the main company data for this sub company.
            company_main = selected_company.company_main
            # Get codes for just this company.
            company_codes = TestCode.objects.filter(company=selected_company)

    elif user.type == User.Types.CLIENT:
        # If a sub client, get only it's own company.
        companies = Company.objects.filter(id=user.company.id)
        # Get company and codes data.
        selected_company = Company.objects.get(id=company_id)
        # Get just users from this sub company.
        company_users = User.objects.filter(Q(company=company_id))
        # Get the main company data for this sub company.
        company_main = selected_company.company_main
        # Get codes for just this company.
        company_codes = TestCode.objects.filter(company=selected_company)

    elif user.type == User.Types.ADMIN_DPE:
        # Get company and codes data.
        selected_company = Company.objects.get(id=company_id)
        # If selected company is a main company, get its data
        companies = Company.objects.filter(Q(id=selected_company.id) | Q(company_main=selected_company.id))
        # Get just users from this sub company.
        company_users = User.objects.filter(Q(company=selected_company.id) | Q(company_main=selected_company.id))
        # Get the main company data.
        company_main = selected_company.company_main
        # Get all codes from this company companies.
        company_codes = TestCode.objects.filter(company=selected_company)

    # GET ASSIGNED TESTS FOR THIS COMPANY
    assigned_tests = CompanyTest.objects.filter(company=selected_company)
    # GET AVAILABLE TEST (EXCLUDING THE TEST THAT ARE ALREADY ASSIGNED TO THIS COMPANY)
    available_tests = TestCatalog.objects.exclude(test_name__in=[test.test.test_name for test in assigned_tests])

    if request.method == 'POST':
        # UPDATE COMPANY 
        if request.POST.get('update'):
            print('update', selected_company)
            selected_company.company_name = request.POST.get('company_name')
            selected_company.company_contact = request.POST.get('company_contact')
            selected_company.company_email = request.POST.get('company_email')
            selected_company.save()

            return render(request,'company/company_detail.html', {
                                                                "company":selected_company,
                                                                "company_main":company_main,
                                                                "company_users":company_users,
                                                                "companies": companies,
                                                                "company_codes":company_codes,
                                                                'user': user,
                                                                'assigned_tests':assigned_tests,
                                                                'available_tests':available_tests,
                                                                'tab':'company',
                                                                })

        # CREATE COMPANY USER 
        elif request.POST.get('create_user'):
            print('create_user')
            form = SignUpForm(request.POST)
            print('form.errors > ',form.errors)
            if form.is_valid():
                form.save()
                
            return render(request,'company/company_detail.html', {
                                                                "company":selected_company,
                                                                "company_main":company_main,
                                                                "company_users":company_users,
                                                                "companies": companies,
                                                                "company_codes":company_codes,
                                                                'user': user,
                                                                'assigned_tests':assigned_tests,
                                                                'available_tests':available_tests,
                                                                'form_errors':form.errors,
                                                                })

        # ASSIGN SELECTED TEST TO THIS COMPANY
        elif request.POST.get('assign_test'):
            print('ASSIGN TEST')
            test_id = request.POST.get('test')
            selected_test = TestCatalog.objects.get(id=test_id)
            # CHECK IF THE TEST IS NO TALREADY ASSIGNED TO THIS COMPANY
            if assigned_tests.filter(test=selected_test).exists():
                print('test already assigned to this copmpany')
                return render(request,'company/company_detail.html', {
                                                            "company":selected_company,
                                                            "company_main":company_main,
                                                            "company_users":company_users,
                                                            "companies": companies,
                                                            "company_codes":company_codes,
                                                            'user': user,
                                                            'assigned_tests':assigned_tests,
                                                            'available_tests':available_tests,
                                                            })
            # IF NOT EXISTS, EVALUATE AND SAVE NEW COMPANYTEST OBJECT
            new_companytest = CompanyTestForm({'company':selected_company,'test':selected_test})
            if new_companytest.is_valid():
                print("is valid")
                new_companytest = new_companytest.save()
                # RE EVALUATE assigned_tests AND available_tests BECAUSE new_companytest CHANGED THOSE TABLES
                assigned_tests = CompanyTest.objects.filter(company=selected_company)
                available_tests = TestCatalog.objects.exclude(test_name__in=[test.test.test_name for test in assigned_tests])

                return render(request,'company/company_detail.html', {
                                                            "company":selected_company,
                                                            "company_main":company_main,
                                                            "company_users":company_users,
                                                            "companies": companies,
                                                            "company_codes":company_codes,
                                                            'user': user,
                                                            'assigned_tests':assigned_tests,
                                                            'available_tests':available_tests,
                                                            'saved_companytest':new_companytest,
                                                            })

        # DELETE TEST ASSIGNED (COMPANYTEST TABLE)
        elif request.POST.get('delete_test'):
            print('DELETE TEST')
            # DELETE THE RELATION
            companytest_id = request.POST.get('companytest_id')
            companytest_object = CompanyTest.objects.filter(id=companytest_id)
            companytest_object.delete()
            # DELETE ALL CODES RELATED TO THIS TEST IN THIS COMPANY
            test_id = request.POST.get('test_id')
            test = TestCatalog.objects.get(id=test_id)
            company_test_codes = TestCode.objects.filter(company=selected_company,test=test)
            company_test_codes.delete()
            # RE EVALUATE assigned_tests AND available_tests BECAUSE companytest_object.delete() CHANGED THOSE TABLES
            assigned_tests = CompanyTest.objects.filter(company=selected_company)
            available_tests = TestCatalog.objects.exclude(test_name__in=[test.test.test_name for test in assigned_tests])
            return render(request,'company/company_detail.html', {
                                                            "company":selected_company,
                                                            "company_main":company_main,
                                                            "company_users":company_users,
                                                            "companies": companies,
                                                            "company_codes":company_codes,
                                                            'user': user,
                                                            'assigned_tests':assigned_tests,
                                                            'available_tests':available_tests,
                                                            'tab':'codes',
                                                            })

        # CREATE NEW CODE
        elif request.POST.get('create_code'):
            print('create code')
            # Concat strings to create the code
            #company_id = request.POST.get('company_id')
            expiration = request.POST.get('expiration')
            date = datetime.fromordinal(733828)
            number_date = date.strftime('%Y%m%d')
            #company = Company.objects.get(id=company_id)
            company = selected_company

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            test_id = request.POST.get('test_id')
            print('test_id',test_id)
            test = TestCatalog.objects.get(id=test_id)
            code = test.test_name[0:5]+"-"+number_date+"-"+company.company_name[0:4]+"-"+expiration.replace("-","")
            new_code = TestCodeForm({'user':user,'company':company,'test':test,'code':code,'activate':True,'expiration':expiration})
            if new_code.is_valid():
                new_code.save()
                print("created new code")
            return render(request,'company/company_detail.html', {
                                                            "company":selected_company,
                                                            "company_main":company_main,
                                                            "company_users":company_users,
                                                            "companies": companies,
                                                            "company_codes":company_codes,
                                                            'user': user,
                                                            'assigned_tests':assigned_tests,
                                                            'available_tests':available_tests,
                                                            'tab':'codes',
                                                            })

        # ACTIVATE/DEACTIVATE CODE
        elif request.POST.get('modify_code'):
            print('activate / deactivate code')
            # get the code from the db
            code_id = request.POST.get('code_id')
            code = TestCode.objects.get(id=code_id)

            if request.POST.get('deactivate_code', False):
                code.activate = False
            else:
                code.activate = True
            # Save the new state
            code.save()

            return render(request,'company/company_detail.html', {
                                                                "company":selected_company,
                                                                "company_main":company_main,
                                                                "company_users":company_users,
                                                                "companies": companies,
                                                                "company_codes":company_codes,
                                                                'user': user,
                                                                'assigned_tests':assigned_tests,
                                                                'available_tests':available_tests,
                                                                'tab':'codes',
                                                                })
        
        # DELETE CODE
        elif request.POST.get('delete_code'):
            print('Delete code')
            # Concat strings to create the code
            code_id = request.POST.get('code_id')
            code = TestCode.objects.get(id=code_id)
            code.delete()

            return render(request,'company/company_detail.html', {
                                                                "company":selected_company,
                                                                "company_main":company_main,
                                                                "company_users":company_users,
                                                                "companies": companies,
                                                                "company_codes":company_codes,
                                                                'user': user,
                                                                'assigned_tests':assigned_tests,
                                                                'available_tests':available_tests,
                                                                'tab':'codes',
                                                                })

        # RESULTS LIST
        elif request.POST.get('select_test_type'):
            print('Select test')
            # Get the test from the request
            test = request.POST.get('test')
            if test == "CIE":
                cie_objects = ObjectCIE.objects.filter(codigo__company=selected_company)

                return render(request,'company/results_list.html', {
                                                            "company":selected_company,
                                                            "company_main":company_main,
                                                            "test":'CIE',
                                                            "cie_objects":cie_objects,
                                                            })


    return render(request,'company/company_detail.html', {
                                                            "company":selected_company,
                                                            "company_main":company_main,
                                                            "company_users":company_users,
                                                            "companies": companies,
                                                            "company_codes":company_codes,
                                                            'user': user,
                                                            'assigned_tests':assigned_tests,
                                                            'available_tests':available_tests,
                                                            })

@login_required
def modify_user(request, company_name):
    """Modify a company user."""
    if request.method == 'POST':
        #Select an user.
        if request.POST.get('company_user_id'):
            print("company_user_id", request.POST.get('company_user_id'))
            user_id = request.POST.get('company_user_id')
            selected_user = User.objects.get(id=user_id)
            print("selectd user", selected_user.first_name)

            args = {
                "user":request.user,
                "selected_user":selected_user,
                "company_name":company_name,
            }

            return render(request, "company/user_detail.html", args)
        #Update user.
        elif request.POST.get('update_user'):
            user_id = request.POST.get('user_id')
            company_user = User.objects.get(id=user_id)
            company_user.username = request.POST.get('username')
            company_user.first_name = request.POST.get('first_name')
            company_user.last_name = request.POST.get('last_name')
            company_user.second_last_name = request.POST.get('second_last_name')
            company_user.email = request.POST.get('email')
            company_user.save()

            args = {
                "selected_user":company_user,
                "company_name":company_name,
                'user': request.user
            }

            return render(request, "company/user_detail.html", args)

@login_required
def list_results(request, company_name):
    """List all users from the selected company."""
    if request.method == 'POST':
        #Select an user.
        if request.POST.get('company_user_id'):
            print("company_user_id", request.POST.get('company_user_id'))
            user_id = request.POST.get('company_user_id')
            selected_user = User.objects.get(id=user_id)
            print("selectd user", selected_user.first_name)

            args = {
                "user":request.user,
                "selected_user":selected_user,
                "company_name":company_name,
            }

            return render(request, "company/user_detail.html", args)
        #Update user.
        elif request.POST.get('update_user'):
            user_id = request.POST.get('user_id')
            company_user = User.objects.get(id=user_id)
            company_user.username = request.POST.get('username')
            company_user.first_name = request.POST.get('first_name')
            company_user.last_name = request.POST.get('last_name')
            company_user.second_last_name = request.POST.get('second_last_name')
            company_user.email = request.POST.get('email')
            company_user.save()

            args = {
                "selected_user":company_user,
                "company_name":company_name,
                'user': request.user
            }

            return render(request, "company/user_detail.html", args)
