from django.shortcuts import render
from apps.categories.models import Category
from apps.movies.models import Movie
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
    context = {
        'category' : category,
        'movies' : movies,
        'home' : home,
        'categories' : categories,
        'page_obj' : page_obj,
    }
    return render(request, 'category_detail.html', context)