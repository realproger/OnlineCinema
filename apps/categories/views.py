from django.shortcuts import render
from apps.categories.models import Category
from apps.movies.models import Movie,Actors
from apps.settings.models import Setting
from django.core.paginator import Paginator

# Create your views here.

def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    categories = Category.objects.all().order_by('?')[:5]
    home = Setting.objects.latest('-id')
    movies = Movie.objects.all().order_by('-id')
    paginator = Paginator(movies, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    actors = Actors.objects.all()
    context = {
        'category' : category,
        'movies' : movies,
        'home' : home,
        'categories' : categories,
        'page_obj' : page_obj,
        'actors' : actors,
    }
    return render(request, 'single-movie.html1', context)

def single_movie(request,id):
    movie = Movie.objects.get(id = id)
    category = Category.objects.all()
    context = {
        'movie' : movie,
       ' category' : category
    }

    return render(request, 'single-movie.html', context)
    