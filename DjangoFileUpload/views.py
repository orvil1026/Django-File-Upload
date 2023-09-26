from django.shortcuts import render,redirect    
from django.contrib.auth.decorators import login_required

def home(request):
    return redirect('accounts:login')

