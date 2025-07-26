from rest_framework import serializers
from watchlist_app import models


class ReviewSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = models.Reviews
        fields = '__all__'
    
    
class MovieLastSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    #reviews = serializers.StringRelatedField(many=True, read_only=True)
    #reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review_detail')

    class Meta:
        model = models.MovieLast
        fields = '__all__'
    
    