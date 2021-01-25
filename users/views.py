#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.views.decorators.http import require_http_methods

#Models
from users.models import User
from company.models import Company, TestCode

def login_view(request):
    """Login view."""
    print("login_view")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate usert.
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request,'login.html', {'error':'Invalid username and password'})
    else:
        # If user is already logged, redirect to dashboard.
        if request.user.is_authenticated:
            return redirect('dashboard')
        #if not take to the log in page.
        return render(request, 'login.html')


@login_required
def users_adm(request):
    print("users_adm")
    all_users = User.objects.all()
    for user in all_users:
        print('user:', user.username)
    print(request.user.id)

    #Get current user to populate form.
    user = request.user
    # Get all availables companies.
    if request.method == 'POST':
        # Update current DPE user.
        if request.POST.get('update_user'):
            print('update')
            user.name = request.POST.get('first_name')
            user.first_name = request.POST.get('first_name')
            user.email = request.POST.get('email')
            user.last_name = request.POST.get('second_last_name')
            user.second_last_name = request.POST.get('second_last_name')
            user.type = request.POST.get('user_type')
            user.company = 1
            user.save()
        # Create DPE user.
        elif request.POST.get('create_user'):
            form = SignUpForm(request.POST)
            print('form.errors()',form.errors)
            if form.is_valid():
                saved_user = form.save()
                print('valid')
            else:
                print('invalid')
                saved_user = ''
            return render(request, 'users/users.html', {
                                                        'user':user,
                                                        'saved_user':saved_user,
                                                        'form_errors': form.errors,
                                                        })
    return render(request, 'users/users.html', {
                                                    'user':user,
                                                    'saved_user':'',
                                                    })

@login_required
def log_out(request):
    """Logout a user view."""
    print("log_out")
    logout(request)
    return redirect('login')


def test_view(request, test_form_token):
    """Start Test view."""
    print("start_test_view")
    if request.method == 'POST':
        participant_name = request.POST['name']
        print("participant",participant_name)
        code = request.POST['test_code']
        print("sended code",code)
        # Look for the code entered in the database
        
        if TestCode.objects.filter(code=code).exists():
            test_code = TestCode.objects.get(code=code)
            print("test_code.test",test_code.test.test_name)
            if test_code.test.test_name == 'CIE':
                return redirect('cie_test',test_code=code)
            if test_code.test.test_name == 'DPECON':
                return redirect('dpecon_test',test_code=code)
        else:
            return render(request,'login.html', {'error':'El codigo no es valido'})

    #if not take to the log in page.
    return render(request, 'login.html')