from django.urls import path
from .views import *

urlpatterns = [
    path('register-f/', registerFarmer, name='registerFarmer'),
    path('register-b/', registerBuyer, name='registerBuyer'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
]
