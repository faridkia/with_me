from django.shortcuts import render, redirect
from django.views.generic import View
from .models import User

class LoginView(View):
    template_name = ''
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('http://localhost:3000')
        return super().dispatch(request, *args, **kwargs)

    def get(self):
        form = 
    def post(self):
        ...

