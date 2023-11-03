from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def homePageView(request):
#     return HttpResponse("Hello world")

def homePageView(request):
    data={
        "title": "Home page",
        "bdata": "Welcome to wscube data",
        "courseList": ["PHP", "Java", "Django"],
        "numbers": [10,20,30,40,50],
        "studentDetails": [
            {"Name": "Pradeep", "Phone": 12232322424},
            {"Name": "Sandeep", "Phone": 12432434234}
        ]
    }
    return render(request, "index.html", data)

def trypageview(request):
    return render(request, "tryindex.html")

def aboutus(request):
    return render(request, "about-us.html")