from django.urls import path
from . import views

app_name = "Upload"
urlpatterns = [
    path('', views.upload_file, name='fileUpload'),
]