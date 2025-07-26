from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MovieLast(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    movie = models.ForeignKey(MovieLast,on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating =   models.TextField() 
    comment = models.TextField() 
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.reviewer},{self.rating}"
 