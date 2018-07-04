from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignInForm, SignUpForm

def sign_in(request):
    form = SignInForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('members:sign-in')
    context = {
        'form':form,
    }

    return render(request, 'sign/sing_in.html', context)

def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.created_user()
            user.save()
            login(request, user)
            return redirect('index')
    context = {
        'form':form,
    }
    return render(request, 'sign/sign_up.html', context)