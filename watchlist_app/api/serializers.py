from rest_framework import serializers
from watchlist_app import models


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField()
     
    class Meta:
        model = models.Reviews
        fields = '__all__'
    
    

    
class MovieLastSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    # reviews = ReviewSerializer(many=True, read_only=True)
    #reviews = serializers.StringRelatedField(many=True, read_only=True)
    #reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.MovieLast
        fields = '__all__'    