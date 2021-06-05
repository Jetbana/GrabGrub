from django.shortcuts import render
from typing import NewType
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer, Order, Food

userAccount = User.objects.get(pk=1)

def index(request):
    return render (request, 'index.html')

def login(request):
    order_objects = Order.objects.all()
    if(request.method =="POST"):
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        accountList = User.objects.filter(username=uname)

        if(len(accountList) > 0):
            authenticateUser = User.objects.get(username = uname)

            if(authenticateUser.getPassword() == pword):
                global userAccount
                userAccount = authenticateUser
                messages.success(request, 'Successfully Logged In!')
                return render(request, 'view_orders.html', {'orders':order_objects})
            else:
                messages.info(request, 'Incorrect Username/Password')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Invalid Login')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def signup(request):
    if(request.method == "POST"):
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        accountList = User.objects.filter(username=uname)

        if(len(accountList) > 0):
            messages.info(request, 'Account already exists!')
            return render(request, 'signup.html')
        else:
            User.objects.create(username = uname, password = pword)
            messages.info(request, 'Account created successfully!')
            return redirect('login')
    else:
        return render(request, 'signup.html')

def view_customer(request):
    customer_objects = Customer.objects.all()
    return render(request, 'view_customer.html')

def view_orders(request):
    order_objects = Order.objects.all()
    return render(request,'view_orders.html', {'orders': order_objects})

def view_details(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'view_details.html', {'o':order})

def view_food(request):
    food_objects = Food.objects.all()
    return render(request,'view_food.html', {'foods': food_objects})

def view_customers(request):
    customer_objects = Customer.objects.all()
    return render(request,'view_customers.html', {'customers': customer_objects})

def delete_order(request, pk):
    Order.objects.filter(pk=pk).delete()
    messages.info(request, 'Order deleted successfully')
    return redirect('view_orders')

def add_order(request):
    order_objects = Order.objects.all()
    customer_objects = Customer.objects.all()
    food_objects = Food.objects.all()
    if (request.method == "POST"):
        customer_pk = request.POST.get('customerpk')
        customer = Customer.objects.get(pk=customer_pk)
        foodname = request.POST.get('foodname')
        food = Food.objects.get(name=foodname)
        qty = request.POST.get('qty')
        payment = request.POST.get('payment')
        Order.objects.create(qty=qty, cust_order=customer, food=food, payment_mode=payment)
        return redirect('view_orders')
        
    else:
        return render(request, 'add_order.html', {'customers':customer_objects, 'foods':food_objects})

def delete_food(request, pk):
    Food.objects.filter(pk=pk).delete()
    return redirect('view_food')

def update_details(request, pk):
    order = get_object_or_404(Order,pk=pk)
    if(request.method == "POST"):
        order.qty = request.POST.get('quantity')
        order.payment_mode = request.POST.get('payment')
        order.save()
        return redirect('view_orders')
    else:
        return render(request, 'update_details.html', {'o':order})

def add_customer(request):
    Customer_objects = Food.objects.all()
    if(request.method == "POST"):
        cname = request.POST.get('name')
        nameList = Customer.objects.filter(name=cname)

        if(len(nameList)) > 0: 
            messages.info(request, 'Customer already exists!')
            return render(request, 'add_customer.html')
            
        else:
            name = request.POST.get('name')
            address = request.POST.get('address')
            city = request.POST.get('city')
            Customer.objects.create(name=name,address=address,city=city)
            return redirect('view_customers')
    else:
        return render (request,'add_customer.html')


def delete_customer(request, pk):
    Customer.objects.filter(pk=pk).delete()
    messages.info(request, 'Customer sucessfully deleted.')
    return redirect('view_customers')




def add_food(request):
    food_objects = Food.objects.all()
    if(request.method == "POST"):
        name = request.POST.get('name')
        foodList = Food.objects.filter(name=name)
        if (len(foodList)) > 0:
            messages.info(request, 'Food already exists!')
            return render(request, 'add_food.html', {'f': Food})
        else:
            description = request.POST.get('description')
            price = request.POST.get('price')
            Food.objects.create(name=name,description=description,price=price)
            return redirect('view_food')
    else:
        return render (request,'add_food.html')

def add_order(request):
    order_objects = Order.objects.all()
    customer_objects = Customer.objects.all()
    food_objects = Food.objects.all()
    if (request.method == "POST"):
        customer_pk = request.POST.get('customerpk')
        customer = Customer.objects.get(pk=customer_pk)

        foodname = request.POST.get('foodname')
        food = Food.objects.get(name=foodname)

        qty = request.POST.get('qty')
        payment = request.POST.get('payment')
        

        Order.objects.create(qty=qty, cust_order=customer, food=food, payment_mode=payment)
        return redirect('view_orders')
    else:
        return render(request, 'add_order.html', {'customers':customer_objects, 'foods':food_objects})

def delete_food(request, pk):
    Food.objects.filter(pk=pk).delete()
    return redirect('view_food')

def update_customer(request, pk):
    customer = get_object_or_404(Customer,pk=pk)
    if (request.method == "POST"):
        customername = request.POST.get('name')
        customerList = Customer.objects.filter(name=customername)
        if (len(customerList)) > 0:
            if customer in customerList:
                customer.name = request.POST.get('name')
                customer.address = request.POST.get('address')
                customer.city = request.POST.get('city')
                customer.save()
                return redirect('view_customers')
            else:
                messages.info(request, 'Customer already exists!')
                return render(request, 'update_customer.html', {'c': customer})
        else:
            customer.name = request.POST.get('name')
            customer.address = request.POST.get('address')
            customer.city = request.POST.get('city')
            customer.save()
            return redirect('view_customers')
    else:
        return render(request, 'update_customer.html', {'c':customer})
        
def update_food(request, pk):
    food = get_object_or_404(Food,pk=pk)
    if (request.method == "POST"):
        foodname = request.POST.get('name')
        foodList = Food.objects.filter(name=foodname)
        
        if (len(foodList)) > 0:
            if food in foodList: 
                food.description = request.POST.get('description')
                food.price = request.POST.get('price')
                food.save()
                return redirect('view_food')                
            else:
                messages.info(request, 'Food already exists!')
                return render(request, 'update_food.html', {'f': food})
        else:
            food.name = foodname
            food.description = request.POST.get('description')
            food.price = request.POST.get('price')
            food.save()
            return redirect('view_food')
    else:
        return render (request,'update_food.html', {'f':food})


