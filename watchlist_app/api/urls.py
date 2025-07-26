from django.urls import path
from .import views

urlpatterns = [
   # path('', views.movie_list,),
   # path('<pk>/', views.movie_detail),
   path('',views.MovieLastCreateView.as_view()),
   path('<pk>/', views.MovieDetailView.as_view()),
   path('reviews/', views.ReviewLastCreateView.as_view()),
   path('reviews/<pk>/', views.ReviewDetailView.as_view()),
]
