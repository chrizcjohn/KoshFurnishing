from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
import re





regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
SpecialSym = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
pat = re.compile(SpecialSym) 
# Create your views here.
def index(request):
    context = {}
    print(request.session.get('email'))
    return render(request, 'index.html', context)

def store(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')

        

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        print(cart)
        request.session['cart'] =cart
        return redirect('store')
    
    
    else:
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] ={}
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
    if request.method == "GET":
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html',{'products':products})

def checkout(request):
    context={}
    return render(request, 'checkout.html', context)

def login(request):
    if request.method =="GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                
                return redirect('index')
            else:
                error_message = 'Email or password invalid!'
        else:
            error_message = 'Email or password invalid!'
        
        print(email,password)
        return render(request,'login.html',{'error':error_message})

def validateCustomer(customer):
    error_message = None
    if (not customer.name):
            error_message = "First name Required !!"
    elif len(customer.name) < 4:
                error_message = "First name must be 4 Characters or more  "
    elif not customer.phone:
            error_message   = " Phone number is required "
    elif len(customer.phone) < 10 or len(customer.phone) > 10:
            error_message = " Phone number must be 10 char Long"
    elif not re.search(regex, customer.email):
            error_message = " Enter valid email id"

    #PASSOWORD VALIDATION    
        # elif len(password) < 8:
        #     error_message = "Password should be 8 char long"
        # elif not re.search(pat, password):
        #     error_message="Password should contain Uppper case character, lower case character, special character and at least a number"
    elif customer.isExists():
        error_message = "Email address already exists"

    return error_message

def signup(request):
    
    if request.method =='GET':
        return render(request, 'registration.html')
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
        
        error_message =  validateCustomer(customer)
        if not error_message: 

            
            customer.password = make_password(customer.password)
            customer.register()
            # return redirect('store')
            return redirect('index')
        else:
            data = {
             'error': error_message,
             'value':value
            }
            return render(request, 'registration.html', data)


def logout(request):
    request.session.clear()
    return redirect('index')
