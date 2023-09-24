from django.shortcuts import render


def home(request):
    return render(request,'login.html')


def fileUpload(request):
    return render(request, 'FileUpload.html')