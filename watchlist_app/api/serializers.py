from rest_framework import serializers
from watchlist_app import models


class MovieLastSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieLast
        fields = '__all__'


 