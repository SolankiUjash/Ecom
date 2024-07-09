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
    totalProduct = product.count()
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    cproduct = totalProduct

    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('filter_price')
    COLOR_ID = request.GET.get('color')
    BRAND_ID = request.GET.get('brand')
    
    if CATID:
        product = product.filter(categories = CATID)
        cproduct  =  product.count()
    elif PRICE_FILTER_ID:
        product = product.filter(filter_price = PRICE_FILTER_ID)
        cproduct  =  product.count()   
    elif COLOR_ID: 
        product = product.filter(color = COLOR_ID)
        cproduct  =  product.count()   
    elif BRAND_ID: 
        product = product.filter(brand = BRAND_ID)
        cproduct  =  product.count()   
    else:
        product = Product.objects.all().filter(status = "PUBLISH")    



    context = {
        'product' : product,
        'categories':categories,
        'cproduct':cproduct,
        'totalProduct':totalProduct,
        'filterprice':filter_price,
        'color':colors,
        'brand':brands
    }
    
    return render(request,"Main/product.html",context)
