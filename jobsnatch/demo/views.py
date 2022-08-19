from django.shortcuts import render
from django.http import HttpResponse

def demo1(request):
    return render(request,'demo1.html',{'name':'don'})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'result.html',{'result':res})
