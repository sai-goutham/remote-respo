from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def Goutham(request):
    date=datetime.datetime.now()
    msg="<h1>Hello</h1><hr>"
    msg=msg+"<h1>servertime is:"+str(date)+"</h1>"
    return HttpResponse(msg)
