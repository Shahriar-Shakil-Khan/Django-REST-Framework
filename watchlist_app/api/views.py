from watchlist_app import models
from .import serializers 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from . import permission



# @api_view()
# def movie_list(request):
#     movies = models.MovieLast.objects.all()
#     serializer = serializers.MovieLastSerializer(movies ,many=True)
#     return Response(serializer.data)



# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = models.MovieLast.objects.all()
#         serializer = serializers.MovieLastSerializer(movies ,many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = serializers.MovieLastSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET','PUT','DELETE','PATCH'])
# def movie_detail(request,pk):
#     movie = get_object_or_404(models.MovieLast, pk=pk)
    
#     if request.method == 'GET':
#          serializer = serializers.MovieLastSerializer(movie)
#          return Response(serializer.data, status=status.HTTP_200_OK)
     
#     elif request.method == 'PUT':
#         serializer = serializers.MovieLastSerializer(movie , data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#              return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
         
#     elif request.method == 'PATCH':
#         serializer = serializers.MovieLastSerializer(movie , data=request.data ,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#              return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)     
    
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response({'message': 'Movie deleted successfully!'})     
            

     
# # list of all movie , create a new movie    
# class MovieLastCreateView(generics.ListCreateAPIView):
#     queryset = models.MovieLast.objects.all()
#     serializer_class = serializers.MovieLastSerializer
     
     
# #singe move /update/delete  
# class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.MovieLast.objects.all()
#     serializer_class = serializers.MovieLastSerializer
    
  
# #list of all reviews, create a new review    
# class ReviewLastCreateView(generics.ListCreateAPIView):
#     queryset = models.Reviews.objects.all()
#     serializer_class = serializers.ReviewSerializer
     
     
# #singe review /update/delete  
# class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Reviews.objects.all()
#     serializer_class = serializers.ReviewSerializer
        

class MovieListViewSet(viewsets.ModelViewSet):
    queryset = models.MovieLast.objects.prefetch_related('reviews')
    serializer_class = serializers.MovieLastSerializer
    


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Reviews.objects.select_related('movie')
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permission.IsReviewerOrReadOnly,IsAuthenticated]
