from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from apps.movies.models import Movie, MovieComment,MovieImage,Actors,LikeProduct
from apps.categories.models import Category
from django.db.models import Q
from apps.movies.forms import MovieCreateForm, MovieUpdateForm
from django.core.mail import send_mail
from apps.settings.models import Setting

# Create your views here.
def movie_detail(request, id):
    movie = Movie.objects.get(id = id)
    random_movies = Movie.objects.all().order_by('?')[:20]
    home = Setting.objects.latest('id')
    categories = Category.objects.all().order_by('?')[:5]
    if 'like' in request.POST:
        try:
            like = LikeProduct.objects.get(user=request.user, movie=movie)
            like.delete()
        except:
            LikeProduct.objects.create(user=request.user, movie=movie)
    if 'comment' in request.POST:
        id = request.POST.get('post_id')
        message = request.POST.get('comment_message')
        comment = MovieComment.objects.create(message=message, movie=movie, user=request.user)
        return redirect('movie_detail', movie.id)

    context = {
        'movie' : movie,
        'random_movies' : random_movies,
        'home' : home,
        'categories' : categories,
    }
    return render(request, 'movies_detail.html', context)

def movie_search(request):
    movies = Movie.objects.all()
    qury_obj = request.GET.get('key')
    home = Setting.objects.latest('id')
    if qury_obj:
        movies = Movie.objects.filter(Q(title__icontains = qury_obj))
    context = {
        'home' : home, 
        'movies' : movies
    }
    return render(request, 'search-movie.html', context)

def movie_create(request):
    form = MovieCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,

    }
    return render(request, 'movies/create.html', context)

def movie_update(request, id):
    movie = Movie.objects.get(id = id)
    form = MovieUpdateForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movie/detail', movie.id)
    context = {
        'form' : form,
    }
    return render(request, 'movies/update.html', context)


def movie_delete(request, id):
    context ={}
 
    obj = get_object_or_404(Movie, id = id)
    if request.method =="POST":

        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "movies/delete.html", context)

def all_movies(request):
    all_movies = Movie.objects.all()
    context = {
        'all_movies' : all_movies,
    }
    return render(request, "movie-full-grid.html", context )
    






