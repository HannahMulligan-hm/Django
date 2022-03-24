from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    context = { 
        "unique_id" : get_random_string(length=16)
        }
    num_clicks= request.session.get('num_clicks',0)
    request.session['num_clicks'] = num_clicks + 1
    return render(request, "rando.html", context)

def clear(request):
    request.session.flush()
    return redirect("/random_word")
# Create your views here.
#clearsessions