from django.shortcuts import render

# here to get our response import Http is used 
from django.http import HttpResponse
# Create your views here.

def yes(request):
	return HttpResponse('gaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa beeeeeeeeeeeee')

def eggs(request):
	return HttpResponse('<h1>egg omlet is the best<h1>')	
	
	