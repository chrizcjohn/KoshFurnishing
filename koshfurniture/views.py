from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={}
    return render(request, 'index.html', context)

def store(request):
    products = None
    categories = Category.objects.all()
    categoryID= request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_id(categoryID)
    else:
        products = Product.get_all_products()

    context = {'products': products, 'categories':categories}
    return render(request, 'store.html', context)
    
def contact(request):
    context={}
    return render(request, 'contact.html', context)

def cart(request):
    context={}
    return render(request, 'cart.html', context)

def checkout(request):
    context={}
    return render(request, 'checkout.html', context)

def login(request):
    context={}
    return render(request, 'login.html', context)
    
def signup(request):
    context={}
    if request.method =='GET':
        return render(request, 'registration.html', context)
    else:
        postDATA = request.POST
        fullname = postDATA.get('fullname')
        email = postDATA.get('email')
        phone = postDATA.get('Phone')
        password = postDATA.get('password')

        print(fullname,email,phone,password)
        return HttpResponse(request.POST)