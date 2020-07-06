from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from twitteruser.models import CustomUser
from .forms import LoginForm, RegisterForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    return render(request, 'LoginPage.html', {
        'form': form
        })

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password1']
            )
            login(request, user)
            return HttpResponseRedirect(reverse('home'))

    else:
        form = RegisterForm()

    return render(request, 'generic_form.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


