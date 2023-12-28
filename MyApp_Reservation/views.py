from django.shortcuts import render,redirect
from .forms import Details_Form
from .forms import BookingForm
from .forms import Payments_Form
from .models import Booking
from .models import Details
from .models import Payments
from django.shortcuts import get_object_or_404
from .forms import CustomerUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home(request):
    return render(request,"index.html")

def deatils_all_bookings(request):
    return render(request,"admin.html")

def DataCustomer(request):
    booking=Booking.objects.all()
    return render(request,"Datacustomers.html",{"booking":booking})

def DataBooking(request):
    customer =Details.objects.all()
    return render(request,"DataBooking.html",{"customer":customer})

def DataPayaments(request):
    payments=Payments.objects.all()
    return render(request,"DataPayment.html",{"payments":payments})




def conform_all(request):
    latest_entry =Booking.objects.last()
    last=Details.objects.last()
    return render(request,'conform.html', {'latest_entry':latest_entry,'last':last})

def complete(request):
    latest_entry =Booking.objects.last()
    last=Details.objects.last()
    return render(request,'success.html',{'latest_entry':latest_entry,'last':last})
   


def customer_details(request):
    if request.method == 'POST':
        form =BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_details')
    else:
        form =BookingForm()
        return render(request,"customer_details.html",{'form':form})

def booking_details(request):
    if request.method == 'POST':
        form=Details_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payments')
    else:
        form=Details_Form()
        return render(request,"booking_details.html",{'form':form})
    

def payments(request):
    if request.method == 'POST':
        form=Payments_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conform_all')
    else:
        form=Payments_Form()
        return render(request,"payments.html",{'form':form})
    




def update_cus(request,pk):
    instance = get_object_or_404(Booking,pk=pk)
    if request.method == 'POST':
        form =BookingForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('DataCustomer')
    else:
        form =BookingForm(instance=instance)
    return render(request, 'customer_details.html', {'form':form})



def delete_cus(request,pk):
    item = get_object_or_404(Booking,pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('DataCustomer')
    return render(request, 'delete.html', {'item':item})



# Seconds

def update(request,pk):
    instance= get_object_or_404(Details, pk=pk)
    if request.method == 'POST':
        form =Details_Form(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('DataBooking')
    else:
        form=Details_Form(instance=instance)
    return render(request, 'booking_details.html', {'form':form})



def delete(request,pk):
    item = get_object_or_404(Details,pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('DataBooking')
    return render(request, 'deletes.html', {'item':item})


# ##############################
def Register(request):
    form=CustomerUser()
    if request.method=="POST":
        form=CustomerUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Sigin Successfully you Go to Login")
            return redirect('/login')
    return render(request,"register.html",{'form':form})

def Login_pages(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successfully")
                return redirect('/')
            else:
                messages.error(request,"invalid Username Successfully")
                return redirect('/login')
        return render(request,"login.html")
    
def logout_pages(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout Successfully")
    return redirect('/')
