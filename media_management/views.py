from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


class UploadView(TemplateView):
    template_name = "media_management/upload.html"


def upload_file(request):
    if request.method == "POST":
        # add request.files to ipfs
        return  HttpResponse("CATS")