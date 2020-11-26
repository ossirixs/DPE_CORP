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


def position_list(request):
    """ List all available positions."""
    return render(request,'dpe/positions.html', {})

