from django.http import HttpResponse
from django.shortcuts import render
 

def hello(request):
    return HttpResponse("Hello world ! ")

 
def runoob(request):
    dictReplyData = {}
    dictReplyData["listTest"] = ["test1", "test2", "test3"]
    return render(request, 'runoob.html', dictReplyData)
