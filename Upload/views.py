from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.http import HttpResponse
from .models import Files
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def upload_file(request):

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            ufile = request.FILES['files']
            uploadedFile = Files.objects.create(files=ufile)
            uploadedFile.save()

            return redirect('Upload:all_files')
    
    else:

        form = UploadFileForm()

    return render(request, 'FileUpload.html', {'form':form})

@login_required()
def all_files(request):
    files = Files.objects.all()
    return render(request, 'all_files.html', {'files':files})

@login_required()
def download_file(request, file_id):
    uploaded_file = Files.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.files, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.files.name}"'
    return response