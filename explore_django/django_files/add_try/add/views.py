from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    data={
        "title": "myadd",
        "another_text": "this is add",
    }
    return render(request, "home.html", data)

