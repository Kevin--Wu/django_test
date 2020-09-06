from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("APP 02 ! \ntest: <a href='https://www.runoob.com/'>点击跳转</a>")