from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


def index(request):
    return render(request, "home/index.html")  #, {"user": request.user})


def about(request):
    return render(request, "home/about.html")
