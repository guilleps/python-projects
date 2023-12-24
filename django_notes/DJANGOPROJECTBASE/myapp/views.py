from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Index')

def hello(request, username, id):
    return HttpResponse('Hello %s y %i' % (username,id))

def about(request):
    return HttpResponse('About')