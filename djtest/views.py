from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    template = loader.get_template("indexs.html")
    return HttpResponse(template.render())

def Bharath(request):
    return HttpResponse("Hello Windows User")

def greet(request, name):
    return render(request, "greet.html", {
        "name":name.capitalize()
    })