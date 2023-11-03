from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    employees = emp.objects.all()

    context = {'employees': employees}
    return render(request, 'home.html', context)