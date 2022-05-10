from django.urls import path
from apps.categories.views import category_detail,single_movie

urlpatterns = [
    path('movie-single/<int:id>',single_movie,name='single-movie')

]
