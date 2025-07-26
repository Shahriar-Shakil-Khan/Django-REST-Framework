from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter


from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('movie', views.MovieListViewSet, basename='movielist')  # <-- Fix here
router.register('review', views.ReviewViewSet, basename='review')       # <-- And here

urlpatterns = [
   path('', include(router.urls)),
   # path('', views.movie_list,),
   # path('<pk>/', views.movie_detail),
   # path('',views.MovieLastCreateView.as_view()),
   # path('<pk>/', views.MovieDetailView.as_view()),
   # path('reviews/', views.ReviewLastCreateView.as_view(), name='review_list'),
   # path('reviews/<pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
]