from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, "indexs.html", {
        "newyear": now.month == 5 and now.day == 21
    })
