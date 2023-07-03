from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    res=HttpResponse("<html><body bgcolor=red><h1><center>welcome to lokeshit</center></h1></body></html>")
    return res