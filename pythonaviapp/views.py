from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def avi(request):
    return render(request,"first.html")