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
    ATOZ = request.GET.get('ATOZ')
    ZTOA = request.GET.get('ZTOA')
    PRICE_ASC = request.GET.get('price_asc')
    PRICE_DESC = request.GET.get('price_desc')
    DATE_ASC = request.GET.get('date_asc')
    DATE_DESC = request.GET.get('date_desc')


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
    elif ATOZ:
        product = product.order_by('name')
    elif ZTOA:
        product = product.order_by('-name')
    elif PRICE_ASC:
        product = product.order_by('price')
    elif PRICE_DESC:
        product = product.order_by('-price')
    elif DATE_ASC:
        product = product.order_by('created_date')
    elif DATE_DESC:
        product = product.order_by('-created_date')
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


def SEARCH(request):
    query = request.GET.get('query')
    if query != "":
        product = Product.objects.filter(name__icontains = query)
        context = {
            'product':product
        }
    else:
        return render(request,"Main/search.html",{})

    return render(request,"Main/search.html",context)

def PRODUCT_DETAIL_PAGE(request,id):
    prod = Product.objects.filter(id = id).first()
    
    context = {
        'prod':prod
    }
    return render(request,"Main/single_product.html",context)
