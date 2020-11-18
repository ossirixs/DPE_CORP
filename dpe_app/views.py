""" Dpe views """
#Django
from django.http import HttpResponse
from django.shortcuts import render, redirect

#Utilities
from datetime import datetime
import json 

def dashboard(request):
    """ Show DPE Dashboard."""
    return render(request,'dpe/dashboard.html', {})

def company_list(request):
    """ List all available companies."""
    if request.method == 'POST':
        if request.POST['company']:
            company_name = request.POST['company']
            return redirect('company_detail' , company_name=company_name)
    return render(request,'dpe/companies.html', {})

def position_list(request):
    """ List all available positions."""
    return render(request,'dpe/positions.html', {})

def company_detail(request,company_name):
    """ Company detail and actions."""

    return render(request,'dpe/company_detail.html', {"company_name":company_name})