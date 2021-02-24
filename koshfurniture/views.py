from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
SpecialSym = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
pat = re.compile(SpecialSym) 
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
        #VALIDATION

        value = {
            'fullname': fullname,
            'email': email,
            'phone': phone,
        }
        
        error_message = None
        

        customer = Customer(name=fullname,
                                email=email,
                                phone=phone,
                                password=password)
        if (not fullname):
            error_message = "First name Required !!"
        elif len(fullname) < 4:
                error_message = "First name must be 4 Characters or more  "
        elif not phone:
            error_message   = " Phone number is required "
        elif len(phone) < 10 or len(phone) > 10:
            error_message = " Phone number must be 10 char Long"
        elif not re.search(regex, email):
            error_message = " Enter valid email id"

        #PASSOWORD VALIDATION    
        # elif len(password) < 8:
        #     error_message = "Password should be 8 char long"
        # elif not re.search(pat, password):
        #     error_message="Password should contain Uppper case character, lower case character, special character and at least a number"
        elif customer.isExists():
            error_message = "Email address already exists"

        if not error_message: 
            print(fullname, email, phone, password)
            
            
            customer.register()
            # return redirect('store')
            return redirect('index')
        else:
            data = {
             'error': error_message,
             'value':value
            }
            return render(request,'registration.html',data)