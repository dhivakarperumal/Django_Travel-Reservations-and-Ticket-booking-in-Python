from django import forms
from .models import Booking
from .models import Details
from .models import Payments
from .models import User
from django.contrib.auth.forms import UserCreationForm


class BookingForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}))
    father_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Fathername'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your  Email'}))
    data_of_birth=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Date of Birth'}))
    age=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Age'}))
    gender=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Gender'}))
    contact=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Contact'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Address'}))
    class Meta:
        model=Booking
        fields=['name','father_name','email' ,'data_of_birth' ,'age' ,'gender' ,'contact' ,'address']


class Details_Form(forms.ModelForm):
    destination_From=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Destination From'}))
    destination_To=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Destination To '}))
    dates=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your  Date'}))
    times=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Time'}))
    how_maney_peoples=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Counts'}))
    kits=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your How maney Kitds'}))
    big_peoples=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your How maney Peoples'}))
    ac_non_ac=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Ac OR Non Ac'}))
    lover_upper_middle=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your lover_upper_middle'}))

    class Meta:
        model=Details
        fields=['destination_From','destination_To','dates' ,'times' ,'how_maney_peoples' ,'kits' ,'big_peoples','ac_non_ac','lover_upper_middle' ]




class Payments_Form(forms.ModelForm):
    upid=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your UPID'}))
    payment_type_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Payment Types '}))
    transection_id=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Transection Id'}))
    amount=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Amount'}))
    send_monay_our_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Name'}))
   

    class Meta:
        model=Payments
        fields=['upid','payment_type_name' ,'transection_id' ,'amount' ,'send_monay_our_name']


class CustomerUser(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
 

    class Meta:
        model=User
        fields=['username','email','password1','password2']