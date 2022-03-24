
from django.shortcuts import render, redirect, HttpResponse
def index(request):
    return render(request,"index.html")

def result(request):
    if request.method == "POST":
        context = {
        'val1' : request.POST["name"],
        'val2' : request.POST["Dojo_location"],
        'val3' : request.POST["favorite_language"],
        'val4' : request.POST["comment"]
        }
        return render(request, "template.html", context)
    return redirect("/see")

def see(request):
    
    return render(request,"template.html")
# Create your views here.

