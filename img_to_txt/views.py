from django.shortcuts import render
from django.http import JsonResponse, response, request
from django.views.generic import FormView
from .forms import *
import pytesseract
from django.views.decorators.csrf import csrf_exempt
try:
    from PIL import Image
except:
    import Image

# Create your views here.
class HomeView(FormView):
    form_class = UploadForm
    template_name = 'index.html'
    success_url = '/'

    # def form_valid(self, form):
    #     upload = self.request.FILES['file']
    #     print(type(pytesseract.image_to_string(Image.open(upload))))
    #     return super().form_valid(form)

@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        response_data = {}
        upload = request.FILES['file']
        content = pytesseract.image_to_string(Image.open(upload))
        response_data['content'] = content
        
        return JsonResponse(response_data)