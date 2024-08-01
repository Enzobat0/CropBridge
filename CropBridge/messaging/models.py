from django.db import models
from users.models import CustomUser

# Create your models here.

class ChatRoom(models.Model):
    farmer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_farmer': True}, related_name='chat_rooms_as_farmer')
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_buyer': True}, related_name='chat_rooms_as_buyer')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.farmer} - {self.buyer}"
    
    
class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.content
    