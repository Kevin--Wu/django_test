from django.http import HttpResponse
from django.shortcuts import render
 

def hello(request):
    return HttpResponse("Hello world ! ")

 
def runoob(request):
    dictReplyData = {}
    dictReplyData	
    return render(request, 'runoob.html', context)
