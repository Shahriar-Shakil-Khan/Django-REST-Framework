from django.db import models

# Create your models here.

class MovieLast(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    movie = models.ForeignKey(MovieLast,on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.CharField(max_length=100)
    rating =   models.TextField() 
    comment = models.TextField() 
    created = models.DateTimeField(auto_now_add=True)
