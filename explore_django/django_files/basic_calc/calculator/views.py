from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.

def index(request):

    c=''
    try:
        if request.method == "POST":
            pass

            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c = n1+n2
            elif opr == '-':
                c = n1-n2
            elif opr == '*':
                c = n1*n2
            elif opr == '/':
                c = n1/n2


    except Exception as e:
        c="Invlid operator"
        print(e)

    print(c)

    return render(request, "calculator.html", {'c': c})