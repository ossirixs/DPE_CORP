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
    args = {
        'user': request.user
    }
    return render(request,'dpe/dashboard.html', args)

@login_required
def position_list(request):
    """ List all available positions."""
    args = {
        'user': request.user
    }
    return render(request,'dpe/positions.html', args)

