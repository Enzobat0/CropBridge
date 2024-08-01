from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from .models import ChatRoom, Message
from base.models import Product
from users.models import CustomUser

def createChatRoom(request, pk):
    product = get_object_or_404(Product, id=pk)
    farmer = product.farmer
    buyer = request.user

    chatRoom = ChatRoom.objects.filter(
        Q(farmer=farmer, buyer=buyer) |
        Q(farmer=buyer, buyer=farmer)
    ).first()
    
    if chatRoom is None:
        chatRoom = ChatRoom.objects.create(farmer=farmer, buyer=buyer)

    return redirect('chatRoomView', pk=chatRoom.id)
    
def buyerChatRoomView(request, pk):
    chatRooms = ChatRoom.objects.filter(buyer = request.user)
    chatRoom = ChatRoom.objects.get(id = pk)
    messages = Message.objects.filter(room=chatRoom).order_by('-id')
    
    if request.method == 'POST':
        content = request.POST['message']
        message = Message.objects.create(room=chatRoom, user=request.user, content=content)
        message.save()
        
        return redirect('buyerChatRoomView', pk=chatRoom.id)
    
    return render(request, 'messaging/buyerChat.html', { 'chatRoom' : chatRoom, 'chatRooms' : chatRooms, 'messages' : messages })

def buyerChatView(request):
    chatRooms = ChatRoom.objects.filter(buyer = request.user)
    
    return render(request, 'messaging/buyerChats.html', { 'chatRooms' : chatRooms })

def farmerChatView(request):
    chatRooms = ChatRoom.objects.filter(farmer = request.user)
    print('Yes')
    
    return render(request, 'messaging/farmerChats.html', { 'chatRooms' : chatRooms })

def farmerChatRoomView(request, pk):
    chatRooms = ChatRoom.objects.filter(farmer = request.user)
    chatRoom = ChatRoom.objects.get(id = pk)
    messages = Message.objects.filter(room=chatRoom).order_by('-id')
    
    if request.method == 'POST':
        content = request.POST['message']
        message = Message.objects.create(room=chatRoom, user=request.user, content=content)
        message.save()
        
        return redirect('farmerChatRoomView', pk=chatRoom.id)
    
    return render(request, 'messaging/buyerChat.html', { 'chatRoom' : chatRoom, 'chatRooms' : chatRooms, 'messages' : messages })
