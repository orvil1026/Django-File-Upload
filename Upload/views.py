from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
from .models import Files

# Create your views here.
def upload_file(request):

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        ufile = request.FILES['files']
        uploadedFile = Files.objects.create(files=ufile)
        uploadedFile.save()

        return HttpResponse("The Student id is "+ str(uploadedFile.pk))
    
    else:

        form = UploadFileForm()

    return render(request, 'FileUpload.html', {'form':form})