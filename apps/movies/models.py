from django.db import models
from apps.categories.models import Category
from apps.users.models import User


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    main_movie_image = models.ImageField(upload_to = 'main_movie_image', blank = True, null = True)
    year_of_issue = models.DateField()
    GENRE_CHOICES = (
        ('Боевики', 'Боевики'),
        ('Комедии', 'Комедии'),
        ('Фантастика/фэнтези', 'Фантастика/фэнтези'),
        ('Мультфильмы', 'Мультфильмы'),
        ('Драма/мелодрама', 'Драма/мелодрама'),
        ('Ужасы', 'Ужасы'),
        ('Детектив/Триллеры', 'Детектив/Триллеры'),
        ('Документальные', 'Документальные'),
    )
    genre = models.CharField(choices=GENRE_CHOICES, default='Боевики', max_length=250)
    rating = models.CharField(max_length=3,verbose_name= "Рейтинг")
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movie_category')
    slug = models.SlugField()
    movie_trailer = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(verbose_name='Возрастное ограничение',blank=True)
    director_film = models.CharField(max_length=55,verbose_name="Режисёр фильма",blank=True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class MovieImage(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_image", null=True)
    movie_image = models.ImageField(upload_to = "movie_image/", null = True, blank = True)

    class Meta:
        verbose_name = "Картинка фильма"
        verbose_name_plural = "Картинки фильмов"

class MovieComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_movie")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_comment" )
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

class Actors(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    birth = models.DateField()
    position = models.CharField(max_length=70)


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Актёр"
        verbose_name_plural = "Актёры"

class LikeProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_favourite_product")
    product = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name="favourite_movies")

