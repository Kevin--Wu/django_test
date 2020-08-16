from django.http import HttpResponse
from django.shortcuts import render
 

def hello(request):
    return HttpResponse("Hello world ! ")

 
def runoob(request):
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    return render(request, "runoob.html", {"views_str": views_str})
