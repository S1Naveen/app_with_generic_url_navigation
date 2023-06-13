from django.shortcuts import render

# Create your views here.

def person_1(request):
    return render(request,'person_1.html')

def person_2(request):
    return render(request,'person_2.html')

 