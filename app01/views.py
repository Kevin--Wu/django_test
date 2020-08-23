from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("APP 01 ! \ntest: <a href='https://www.runoob.com/'>点击跳转</a>")

# 参数顺序随意
def testparam(request, testalpha, testnum):
    return HttpResponse("Test num is {}, alpha is {}".format(testnum, testalpha))
