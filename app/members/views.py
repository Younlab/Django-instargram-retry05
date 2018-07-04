from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignInForm
def sign_in(request):
    form = SignInForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('members:sign-in')
        else:
            return redirect('members:sign-in')
    context = {
        'form':form,
    }
    return render(request, 'sign/sing_in.html', context)
