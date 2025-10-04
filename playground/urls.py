from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('service/',views.service)

]