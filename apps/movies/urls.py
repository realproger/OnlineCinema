from django.urls import path
from apps.movies.views import all_movies, movie_search,movie_detail

urlpatterns = [
    path('movie_full-grid/',all_movies, name='movie_full-grid'),
    path( 'search/', movie_search, name='search_movie'),
    path('movies-detail/<int:pk>/', movie_detail, name = 'movies-detail')

]


