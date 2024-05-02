from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from .models import User



def home(request):
    return HttpResponse(f'Salam{request.user.username}')
class LoginView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form':form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('accounts:home')
            message = 'Login failed!'
        return render(request, 'accounts/login.html', context={'form': form})


class SignUpView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = SignUpForm()
        return render(request, 'accounts/sing-in.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('accounts:home')
        return render(request, 'accounts/sing-in.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('accounts:home')