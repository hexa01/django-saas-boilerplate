from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from ..forms import RegisterForm, LoginForm


def register_view(request):

    if request.user.is_authenticated:
        return redirect('core:dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            login(request,user)
            return redirect("core:dashboard")
        
    else:
        form = RegisterForm()

    return render(request, 'core/auth/register.html', {'form': form})



def login_view(request):

    if request.user.is_authenticated:
        return redirect('core:dashboard')

    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_deleted == True:
                messages.error(request, 'This user is disabled')
            else:
                login(request,user)
                return redirect("core:dashboard")
    
    else:
        form = LoginForm()

    return render(request, 'core/auth/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('core:login')