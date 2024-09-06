from django.shortcuts import render

# here to get our response import Http is used 
from django.http import HttpResponse
# Create your views here.

def yes(request):
	return render(request, 'generator/home.html')

def eggs(request):
	return HttpResponse('<h1>eggs godd ye s approves<h1>')	