#Django.
from django.shortcuts import render, redirect

#Utilities.
from datetime import datetime

#Models.
from company.models import Company

#Forms
from company.forms import NewCompanyForm

def company_list(request):
    """ List all available companies."""
    print("listing")
    companies = Company.objects.all()
    if request.method == 'POST':
        action = request.POST.get('action','')
        #Company selected.
        if action == "select":
            company_name = request.POST['company']
            return redirect('company_detail' , company_name=company_name)
        #Create a company.
        elif action == "create":
            print('create')
            #form = NewCompanyForm(request.POST)
            new_company = Company(
                company_type = request.POST.get('company-type'),
                company_name = request.POST.get('company-name'), 
                company_contact = request.POST.get('company-contact'), 
                company_phone = request.POST.get('company-phone'), 
                company_email = request.POST.get('company-email'), 
                company_main = request.POST.get('company-main'), 
            )
            new_company.save()

            return render(request,'company/companies.html', {
                                                                'companies':companies,
                                                            })
    return render(request,'company/companies.html', {
                                                        'companies':companies,
                                                    })

def company_detail(request,company_name):
    """ Company detail and actions."""

    return render(request,'company/company_detail.html', {"company_name":company_name})