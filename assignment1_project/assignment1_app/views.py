from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return HttpResponse("This was not worth what I paid")

def show(request, number):
    return HttpResponse("placeholder to display blog number:{number}")

def edit(request, number):
    return HttpResponse("placeholder to edit blog{number}")
# Create your views here.

def destroy(request):
    return HttpResponse("idk how to do this")
