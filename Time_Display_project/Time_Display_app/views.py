from django.shortcuts import render
from time import gmtime, strftime
def index(request):
    context = {
        "time": strftime("%I:%M:%S %p %m %d, %Y ",gmtime())
    }
    return render(request, "index.html", context)

# Create your views here.
