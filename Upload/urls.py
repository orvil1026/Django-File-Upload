from django.urls import path
from . import views

app_name = "Upload"
urlpatterns = [
    path('', views.upload_file, name='fileUpload'),
    path("files/", views.all_files, name="all_files"),
    path("download/<int:file_id>", views.download_file, name="download_file")
]