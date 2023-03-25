from django.shortcuts import render ,redirect
from .forms import Regesterion
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.http import JsonResponse
import json
import datetime
def Regester(request):
    #  لو فعلا البيانات مبعوته عن طريق بوست
    # ابعت البيانات ال جايه من الريقويست لل فورمز 
    # وهاتلي من الفورم الحقول ال هبعتها لل تمبلت ك كونتكست
    if request.method == 'POST' :
        form = Regesterion(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request,'تم تسجيل الدخول بنجاح!')
            # اللوجين ال هبعتها ف الري دايركت جيا من النيم بتاع اليو ار ال 
            return redirect('login')
    else :
        form = Regesterion()
    return render(request,'Regester.html',{'form':form})


def loginion(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       x = authenticate(request,username=username,password=password)
       if x is not None :
            login(request,x)
            messages.success(request,'تم التسجيل')
            return redirect('home')
    return render(request,'Login.html')

@login_required(login_url='accounts/login/')
def Home(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.first_name
    }
    return render(request,'home.html',context)


def logoutUser(requeset):
    logout(requeset)
    return redirect('login')
    

def Store(request ):
    if request.user.is_authenticated :
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer,complate=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else : 
        items = []
        order = {'get_cart_total':0,'get_cart_items':0 ,'shipping':False}
        cartItems = order['get_cart_items']


    data_of_prodict = Product.objects.all()
    len_item = len(data_of_prodict)
    print(len_item)
    cout = request.user
    x = str(cout)
    username = request.session.get('username',None)
    print(username)
    context = {'data':data_of_prodict , 'count':len_item , 'cartItems':cartItems }

    return render(request,'Store/Store.html',context)
























def Cart(request):
    if request.user.is_authenticated:
       customer = request.user.customer
       order , created = Order.objects.get_or_create(customer=customer,complate=False)
       print(type(order))
       item = order.orderitem_set.all()
       cartItems = order.get_cart_items

    else :
       item = []
       order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
       cartItems = order['get_cart_items']

    context = {'item':item,'order':order,'cartItems':cartItems}
    return render(request,'Store/Cart.html',context)



def Checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer,complate=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

        
    else : 
        items = []
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']

        
    context = {'items':items,'order':order,'cartItems':cartItems}
    return render(request,'Store/Checkout.html',context)


def updateData(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    print('PRODUCT => ',product_id)
    print('ACTION  => ',action)

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer,complate=False)

    # get the order item instance, or create a new one if it doesn't exist
    order_items = OrderItem.objects.filter(order=order, product=product)
    if order_items.exists():
        order_item = order_items.first()
        created = False
    else:
        order_item = OrderItem.objects.create(order=order, product=product)
        created = True

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse({'message': 'Item was added', 'created': created}, status=200)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complate=False)
        total = float( data['form']['total'])
        order.transaction_id = transaction_id
        if total == order.get_cart_total:
            order.complate = True
        order.save()
        if order.shipping == True :
            ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
          
            )
    else:
        print('user not authticated')
    return JsonResponse('paymeent complete ', safe = False)
