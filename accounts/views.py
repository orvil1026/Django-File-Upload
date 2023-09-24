from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.


def register_user(request):

    if request.method == 'POST':
        check1=False
        check2=False
        check3=False

        form = UserRegistration(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['renter_password']
            email = form.cleaned_data['email']

            if password1!=password2:
                check1 = True
                messages.error(request,'Password doesnt match!',
                                extra_tags='alert alert-warning alert-dismissible fade show ')

            if User.objects.filter(email=email).exists():
                check2 = True
                messages.error(request,'Email already exists!',
                                extra_tags='alert alert-warning alert-dismissible fade show ')

            if User.objects.filter(username=username).exists():
                check3 = True
                messages.error(request,'Username already exists!',
                                extra_tags='alert alert-warning alert-dismissible fade show ')
            
            if check1 or check2 or check3:

                messages.error(request,'Registration failed!',
                               extra_tags='alert alert-warning alert-dismissible fade show')

                return redirect('accounts:register')
            
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                messages.success(request,'Thanks for registering!',
                                extra_tags='alert alert-success alert-dismissible fade show')
                return redirect('login')
    

    else:
        form=UserRegistration()
    return render(request,'register.html',{'form':form})



def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
          
        if user is not None:
            
            login(request, user)
            redirect_url = request.GET.get('next', 'fileUpload')
            return redirect(redirect_url)
            
                     
        else:
            messages.error(request, "Username or password is not correct",
                            extra_tags ='alert alert-warning alert-dismissible fade show')

    return render(request,'login.html')     