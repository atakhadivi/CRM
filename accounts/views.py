from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log user in and redirect to homepage
            return redirect('home')
    else:
        form = RegistrationForm()
        
    return render(request, 'accounts/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        # else:
        #     # Return error message
    return render(request, 'accounts/login.html')



def logout_view(request):
  logout(request)
  return redirect('login')