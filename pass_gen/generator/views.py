from django.shortcuts import render

# here to get our response import Http is used 
from django.http import HttpResponse
# Create your views here.

def yes(request):
	return render(request, 'generator/home.html', {'password': 'amfnevnwm'})

# so basically the password code is for making a dictonary and we can now pass a key in the home html
# and put keys and get password as per say 

def eggs(request):
	return HttpResponse('<h1>eggs godd ye s approves<h1>')	