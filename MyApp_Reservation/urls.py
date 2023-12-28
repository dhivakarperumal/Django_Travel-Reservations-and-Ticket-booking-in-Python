from django.urls import path
from .import views



urlpatterns = [
    path('',views.home,name="home"),
    path('customer_details/',views.customer_details,name="customer_details"),
    path('booking_details/',views.booking_details,name="booking_details"),
    path('payments/',views.payments,name="payments"),
    path('conform_all/',views.conform_all,name="conform_all"),
    path('deatils_all_bookings/',views.deatils_all_bookings,name="deatils_all_bookings"),
    path('DataCustomer/',views.DataCustomer,name="DataCustomer"),
    path('DataBooking/',views.DataBooking,name="DataBooking"),
    path('DataPayaments/',views.DataPayaments,name="DataPayaments"),
    path('complete',views.complete,name="complete"),
    
    path('item/<int:pk>/update_cus/',views.update_cus, name="update_cus"),
    path('item/<int:pk>/delete_cus/',views.delete_cus, name="delete_cus"),

    path('item/<int:pk>/update/',views.update, name="update"),
    path('item/<int:pk>/delete/',views.delete, name="delete"),

    path('Register', views.Register, name='Register'),
    path('login',views.Login_pages,name="login"),
    path('logout',views.logout_pages,name="logout"),


    
    

]