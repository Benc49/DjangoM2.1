from django.http import HttpResponse, response
from django.http.request import HttpRequest
from django.shortcuts import render

# Create your views here.

def lp(request: HttpRequest, leadership):
    if leadership == "documentation":
        return render(request, "documentation.html")
    elif leadership == "community":
        return render(request, "community.html")
    elif leadership == "management":
        return render(request, "management.html")
    elif leadership == "procurement":
        return render(request, "procurement.html")
