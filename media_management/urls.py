from django.urls import path

from . import views

app_name = "media_management"
urlpatterns = [
    path('upload-page/', views.UploadView.as_view(), name='upload-page'),
    path('upload/', views.upload_file, name='upload'),
]