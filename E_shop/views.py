from django.shortcuts import render,redirect
from django.http import *
from store_app.models import *

def BASE(request):
    return render(request,"Main/base.html",{})

def HOME(request):
    product = Product.objects.all().filter(status = "PUBLISH")
    context = {
        'product' : product,
    }
    return render(request,"Main/index.html",context)

def PRODUCT(request):
    product = Product.objects.all().filter(status = "PUBLISH")
    

    context = {
        'product' : product,
        
    }
    
    return render(request,"Main/product.html",context)
