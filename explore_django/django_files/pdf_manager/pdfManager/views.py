# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from wsgiref.util import FileWrapper

def home(request):
    # if request.method == 'POST':
    #     file = request.POST['file']
    return render(request, "index.html")

def downloadfile(request):
    thefile = filepath
    filename = os.path.basename(thefile)
