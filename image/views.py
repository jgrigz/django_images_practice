from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    template_name = "index.html"
    images = Image.objects.all()
    context = {"images": images}
    return render(request, template_name, context)

def test(request):
    template_name = "test.html"
    images = Image.objects.all()
    context = {"images": images}
    return render(request, template_name, context)