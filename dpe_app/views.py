""" Dpe views """
#Django
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#Utilities
from datetime import datetime
import json 

@login_required
def dashboard(request):
    """ Show DPE Dashboard."""
    return render(request,'dpe/dashboard.html', {})

@login_required
def position_list(request):
    """ List all available positions."""
    return render(request,'dpe/positions.html', {})

