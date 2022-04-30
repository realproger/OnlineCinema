from django.shortcuts import render
from apps.settings.models import Setting, About
from apps.movies.models import Movie, MovieComment
from apps.categories.models import Category
# Create your views here.

def index(request):
    home = Setting.objects.latest('id')
    slide_movies = Movie.objects.all().order_by('-id')[:5]
    movies = Movie.objects.all().order_by('-id')[:8]
    one_random_movie = Movie.objects.all().order_by('?')
    one_random_genre = Movie.objects.all().order_by('?')[:1]
    categories = Category.objects.all().order_by('-id')
    most_popular_movie = Movie.objects.all().order_by('-genre')
    comments = MovieComment.objects.all().order_by('-id')
    context = {
        'home' : home,
        'movies' : movies,
        'slide_movies' : slide_movies,
        'one_random_movie' : one_random_movie,
        'one_random_genre' : one_random_genre,
        'categories' : categories,
        'most_popular_movie' : most_popular_movie,
        'comments' : comments,

    }
    return render(request, 'index.html', context)

def about(request):
    home = Setting.objects.latest('-id')
    about = About.objects.latest('id')
    context = {
        'home' : home,
        'about' : about, 
    }

    return render(request, 'about.html', context)
