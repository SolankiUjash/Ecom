from django.shortcuts import render,redirect
from django.http import *

def BASE(request):
    return render(request,"Main/base.html",{})

def HOME(request):
    return render(request,"Main/index.html",{})