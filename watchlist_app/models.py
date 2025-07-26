from django.db import models

# Create your models here.

class MovieLast(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
