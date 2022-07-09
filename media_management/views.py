from django.views.generic import TemplateView

# Create your views here.


class UploadView(TemplateView):
    template_name = "media_management/upload.html"
