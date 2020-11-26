#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm

#Models
from users.models import User
from company.models import Company

def login_view(request):
    """Login view."""
    print(request.method)
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
    else:
        print('else')
        return render(request, 'login.html')


@login_required
def users_adm(request):

    all_users = User.objects.all()
    for user in all_users:
        print('user:', user.username)
    print(request.user.id)

    #Get current user to populate form.
    current_user_id = request.user.id
    user = User.objects.get(id=current_user_id)
    # Get all availables companies.
    companies = Company.objects.all()

    if request.method == 'POST':
        print('a posst')
        if request.POST.get('update_user'):
            print('update')
            print(request.POST.get('company'))
            user.name = request.POST.get('first_name')
            user.first_name = request.POST.get('first_name')
            user.email = request.POST.get('email')
            user.last_name = request.POST.get('second_last_name')
            user.second_last_name = request.POST.get('second_last_name')
            user.type = request.POST.get('user_type')
            user.company = request.POST.get('company')
            user.save()
        elif request.POST.get('create_user'):
            print('create')
            form = SignUpForm(request.POST)
            print('form.errors()',form.errors)
            if form.is_valid():
                form.save()
                # username = form.cleaned_data.get('username')
                # password = form.cleaned_data.get('password1')
                # user = authenticate(username=username, password=password)
                # login(request, user)
            


    return render(request, 'users/users.html', {
                                                'username':user.username,
                                                'name':user.name,
                                                'first_name':user.first_name,
                                                'last_name':user.last_name,
                                                'second_last_name':user.second_last_name,
                                                'email':user.email,
                                                'user_type':user.type,
                                                'user_types':user.Types,
                                                'user_company':user.company,
                                                'companies':companies,
                                                })
