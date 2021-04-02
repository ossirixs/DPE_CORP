#Django.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models import Q
from datetime import datetime, date
from django.http import HttpResponseRedirect
from django.http import HttpResponse
#Models.
from company.models import Company, TestCode, CompanyTest, TestCatalog
from users.models import User
from tests.models import ObjectCIE, ObjectIntegrity, ObjectMax, MaxPositions
#Forms
from company.forms import NewCompanyForm, TestCodeForm, CompanyTestForm
from users.forms import SignUpForm
from users.models import User
#Utils
from company.utils import get_integrity_export_data
#Libraries
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

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
def company_detail(request,company_id,tab='tests'):
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
    # Get the max positions for this company
    max_positions = MaxPositions.objects.filter(company=selected_company)
    # Get optional return tab from POST or GET.
    if request.POST.get('tab'):
        tab = request.POST.get('tab')

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
                                                                'max_positions':max_positions,
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
                                                                'max_positions':max_positions,
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
                                                            'max_positions':max_positions,
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
                                                            'max_positions':max_positions,
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
                                                            'max_positions':max_positions,
                                                            'tab':'codes',
                                                            })

        # CREATE NEW CODE
        elif request.POST.get('create_code'):
            print('create code')
            # Concat strings to create the code
            #company_id = request.POST.get('company_id')
            expiration = request.POST.get('expiration', '')
            date = datetime.fromordinal(733828)
            number_date = date.strftime('%Y%m%d')
            #company = Company.objects.get(id=company_id)
            company = selected_company

            now = datetime.now()
            current_time_ml = now.strftime("%f")

            test_id = request.POST.get('test_id')
            test = TestCatalog.objects.get(id=test_id)
            code = test.test_name+"-"+number_date+"-"+company.company_name[0:4]+"-"+expiration.replace("-","")+current_time_ml
            if test.test_name == 'Integridad':
                seconds_integrity = request.POST.get('seconds_integrity', 0)
            else:
                seconds_integrity = 0
            new_code = TestCodeForm({'user':user,'company':company,'test':test,'code':code,'activate':True,'expiration':expiration,'seconds_integrity':int(seconds_integrity)})
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
                                                            'max_positions':max_positions,
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
                                                                'max_positions':max_positions,
                                                                'tab':'codes',
                                                                })
        
        # DELETE CODE
        elif request.POST.get('delete_code'):
            print('Delete code')
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
                                                                'max_positions':max_positions,
                                                                'tab':'codes',
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
                                                            'max_positions':max_positions,
                                                            'tab':tab,
                                                            })

@login_required
def test_results_list(request, company_id):
    """List all test results from the selected company."""
    #Select a test type.
    if request.method == 'POST':
        if request.POST.get('select_test'):
            test = request.POST.get('test', False)
            company_id = request.POST.get('company', False)
            selected_company = Company.objects.get(id=company_id)
            if test and company_id:
                print("test_type", test)
                if test == "CIE":
                    cie_objects = ObjectCIE.objects.filter(codigo__company=selected_company)

                    return render(request,'company/results_list.html', {
                                                                "company":selected_company,
                                                                "company_main":selected_company.company_main,
                                                                "test":'CIE',
                                                                "cie_objects":cie_objects,
                                                                })
                if test == "Integridad":
                    integrity_objects = ObjectIntegrity.objects.filter(code__company=selected_company)

                    return render(request,'company/results_list.html', {
                                                                "company":selected_company,
                                                                "company_main":selected_company.company_main,
                                                                "test":'Integridad',
                                                                "integrity_objects":integrity_objects,
                                                                })
                if test == "Max":
                    max_objects = ObjectMax.objects.filter(code__company=selected_company)

                    return render(request,'company/results_list.html', {
                                                                "company":selected_company,
                                                                "company_main":selected_company.company_main,
                                                                "test":'Max',
                                                                "max_objects":max_objects,
                                                                })
        if request.POST.get('filter_results'):
            test = request.POST.get('test', False)
            company_id = request.POST.get('company_id', False)
            selected_company = Company.objects.get(id=company_id)
            if test and company_id:
                if test == "CIE":
                    cie_objects = ObjectCIE.objects.filter(codigo__company=selected_company)
                    applicant_name = request.POST.get('applicant_name', '')
                    test_date = request.POST.get('test_date', '')
                    if applicant_name:
                        cie_objects = cie_objects.filter(nombre__contains=applicant_name)
                    if test_date:                        
                        cie_objects = cie_objects.filter(created__date=test_date)

                    return render(request,'company/results_list.html', {
                                                                "company":selected_company,
                                                                "company_main":selected_company.company_main,
                                                                "test":'CIE',
                                                                "cie_objects":cie_objects,
                                                                "test_date":test_date,
                                                                "applicant_name":applicant_name,
                                                                })

                if test == "Integridad":
                    integrity_objects = ObjectIntegrity.objects.filter(code__company=selected_company)
                    applicant_name = request.POST.get('applicant_name', '')
                    test_date = request.POST.get('test_date', '')
                    if applicant_name:
                        integrity_objects = integrity_objects.filter(name__contains=applicant_name)
                    if test_date:                        
                        integrity_objects = integrity_objects.filter(created__date=test_date)

                    return render(request,'company/results_list.html', {
                                                                "company":selected_company,
                                                                "company_main":selected_company.company_main,
                                                                "test":'Integridad',
                                                                "integrity_objects":integrity_objects,
                                                                "test_date":test_date,
                                                                "applicant_name":applicant_name,
                                                                })

                if test == "Max":
                    max_objects = ObjectMax.objects.filter(code__company=selected_company)
                    applicant_name = request.POST.get('applicant_name', '')
                    test_date = request.POST.get('test_date', '')
                    if applicant_name:
                        max_objects = max_objects.filter(name__contains=applicant_name)
                    if test_date:                        
                        max_objects = max_objects.filter(created__date=test_date)

                    return render(request,'company/results_list.html', {
                                                                "company":selected_company,
                                                                "company_main":selected_company.company_main,
                                                                "test":'Max',
                                                                "max_objects":max_objects,
                                                                "test_date":test_date,
                                                                "applicant_name":applicant_name,
                                                                })
        if request.POST.get('export_xlsx'):
            result_ids = request.POST.get('result_ids', '')
            result_ids = result_ids.split(',')
            print('test results to export ',result_ids)
            result_ids.remove('')
            wb = Workbook()
            ws = wb.active
            ws.title = "New Title"
            ws.append(['Nombre' , 'Fecha', 'Adicciones', 'Adicciones', 'Lealtad', 'Lealtad', 'Intencionalidad', 'Intencionalidad', 'Seguridad', 'Seguridad', 'Disciplina', 'Disciplina', 'Etica', 'Etica', 'Veracidad', 'Veracidad', 'Juicio', 'Juicio', 'Codigo'])
            if result_ids:
                for result_id in result_ids:
                    test_result = ObjectIntegrity.objects.get(id=int(result_id))
                    integrity_export_data = get_integrity_export_data(test_result)
                    ws.append([test_result.name, test_result.get_formated_created, 
                                integrity_export_data['scores']['addictions_score'], integrity_export_data['percentages']['addictions_percentage'], 
                                integrity_export_data['scores']['judgement_score'], integrity_export_data['percentages']['judgement_percentage'] ,
                                integrity_export_data['scores']['discipline_score'], integrity_export_data['percentages']['discipline_percentage'] ,
                                integrity_export_data['scores']['veracity_score'], integrity_export_data['percentages']['veracity_percentage'] ,
                                integrity_export_data['scores']['loyalty_score'], integrity_export_data['percentages']['loyalty_percentage'],
                                integrity_export_data['scores']['intentionality_score'], integrity_export_data['percentages']['intentionality_percentage'] ,
                                integrity_export_data['scores']['ethic_score'], integrity_export_data['percentages']['ethic_percentage'],
                                integrity_export_data['scores']['reliability_score'], integrity_export_data['percentages']['reliability_percentage'],
                                test_result.code.code])



            response = HttpResponse(content=save_virtual_workbook(wb), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=myexport.xlsx'
            return response

    return redirect('dashboard')
        

@login_required
def modify_user(request, company_id):
    """Modify a company user."""
    if request.method == 'POST':
        company = Company.objects.get(id=company_id)
        #Select an user.
        if request.POST.get('company_user_id'):
            print("company_user_id", request.POST.get('company_user_id'))
            user_id = request.POST.get('company_user_id')
            selected_user = User.objects.get(id=user_id)
            print("selectd user", selected_user.first_name)

            args = {
                "user":request.user,
                "selected_user":selected_user,
                "company":company,
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
                "company":company,
                'user': request.user
            }

            return render(request, "company/user_detail.html", args)

@login_required
def modify_position(request, company_id):
    """Modify a company user."""
    print('modify_position')
    company = Company.objects.get(id=company_id)
    if request.method == 'POST':
        # Update position.
        if request.POST.get('update_position'):
            position_id = request.POST.get('position_id')
            selected_position = MaxPositions.objects.get(id=position_id)
            selected_position.T = request.POST.get('T',0)
            selected_position.V = request.POST.get('V',0)
            selected_position.X = request.POST.get('X',0)
            selected_position.S = request.POST.get('S',0)
            selected_position.B = request.POST.get('B',0)
            selected_position.O = request.POST.get('O',0)
            selected_position.R = request.POST.get('R',0)
            selected_position.D = request.POST.get('D',0)
            selected_position.C = request.POST.get('C',0)
            selected_position.Z = request.POST.get('Z',0)
            selected_position.E = request.POST.get('E',0)
            selected_position.K = request.POST.get('K',0)
            selected_position.F = request.POST.get('F',0)
            selected_position.W = request.POST.get('W',0)
            selected_position.N = request.POST.get('N',0)
            selected_position.G = request.POST.get('G',0)
            selected_position.A = request.POST.get('A',0)
            selected_position.L = request.POST.get('L',0)
            selected_position.P = request.POST.get('P',0)
            selected_position.I = request.POST.get('I',0)
            selected_position.save()

            return redirect('company_detail' , company_id=company.id, tab='positions')

        # Create new Max position
        elif request.POST.get('create_position'):
            new_position = MaxPositions(
                company=company,
                position_name=request.POST.get('name',''),
                T = request.POST.get('T',0),
                V = request.POST.get('V',0),
                X = request.POST.get('X',0),
                S = request.POST.get('S',0),
                B = request.POST.get('B',0),
                O = request.POST.get('O',0),
                R = request.POST.get('R',0),
                D = request.POST.get('D',0),
                C = request.POST.get('C',0),
                Z = request.POST.get('Z',0),
                E = request.POST.get('E',0),
                K = request.POST.get('K',0),
                F = request.POST.get('F',0),
                W = request.POST.get('W',0),
                N = request.POST.get('N',0),
                G = request.POST.get('G',0),
                A = request.POST.get('A',0),
                L = request.POST.get('L',0),
                P = request.POST.get('P',0),
                I = request.POST.get('I',0),
            )
            new_position.save()
            return redirect('company_detail' , company_id=company.id)
        
        # Delete selected position.
        elif request.POST.get('delete_position'):
            position_id = request.POST.get('position_id')
            selected_position = MaxPositions.objects.get(id=position_id)
            selected_position.delete()
            return redirect('company_detail' , company_id=company.id)
        # Show position.
        else:
            position_id = request.POST.get('position_id')
            selected_position = MaxPositions.objects.get(id=position_id)

            args = {
                "user":request.user,
                "selected_position":selected_position,
                "company":company,
                "create":0,
            }

            return render(request, "company/position_detail.html", args)
    # Create mode
    else:
        args = {
            "user":request.user,
            "selected_position":{},
            "company":company,
            "create":1,
        }

        return render(request, "company/position_detail.html", args)
            

@login_required
def list_results(request, company_id):
    """List all users from the selected company."""
    if request.method == 'POST':
        # Get the company.
        company = Company.objects.get(id=company_id)
        #Select an user.
        if request.POST.get('company_user_id'):
            user_id = request.POST.get('company_user_id')
            selected_user = User.objects.get(id=user_id)

            args = {
                "user":request.user,
                "selected_user":selected_user,
                "company":company,
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
                "company":company,
                'user': request.user
            }

            return render(request, "company/user_detail.html", args)
