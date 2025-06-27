from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
from django.shortcuts import  render
def index(request):
    name = "world"
    return render(request, "base.html", {"name": name})



def index1(request):
    return HttpResponse("abc")