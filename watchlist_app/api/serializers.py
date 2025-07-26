from rest_framework import serializers
from watchlist_app import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reviews
        fields = '__all__'
    
    
class MovieLastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieLast
        fields = '__all__'
    
    