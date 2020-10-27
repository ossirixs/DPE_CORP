#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def login_view(request):
    """Login view."""
    if request.method == 'POST':
      print('+' * 10)
      username = request.POST['username']
      password = request.POST['password']
      print(username,':',password)
      print('+' * 10)
      user = authenticate(request, username=username, password=password)
      if user:
        login(request, user)
        return redirect('dashboard')
      else:
        return render(request,'login.html', {'error':'Invalid username and password'})
      #import pdb; pdb.set_trace()
    return render(request, 'login.html')



def dashboard(request):
    return render(request, 'dashboard.html', {})
