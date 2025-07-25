from django.shortcuts import render, redirect
from django.contrib.auth import  logout
from django.contrib.auth.decorators import login_required
from .forms import  LoginForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from .forms import AdminLoginForm, RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if not form.cleaned_data['remember_me']:
                request.session.set_expiry(0)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {
        'user': request.user
    })


def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('admin_dashboard')
    else:
        form = AdminLoginForm()
    return render(request, 'accounts/admin_login.html', {'form': form})

@user_passes_test(lambda u: u.is_admin_account)
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')