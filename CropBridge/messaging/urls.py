from django.urls import path
from .views import *

urlpatterns = [
    path('find-create-chatroom/<str:pk>/', createChatRoom, name='createRoom'),
    path('buyer/<str:pk>/', buyerChatRoomView, name='buyerChatRoomView'),
    path('farmer/<str:pk>/', farmerChatRoomView, name='farmerChatRoomView'),
    path('buyer/', buyerChatView, name='buyerChatView'),
    path('farmer/', farmerChatView, name='farmerChatView'),
]
