from django.contrib import admin
from apps.movies.models import Movie, MovieImage, MovieComment

# Register your models here.

class MovieImageAdmin(admin.TabularInline):
    model = MovieImage
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [MovieImageAdmin]
    list_display = ('title', 'genre')
    search_fields = ('title', 'genre')
    ordering = ('-genre',)
    list_per_page = 4
    prepopulated_fields = {"slug": ('title', )}

admin.site.register(Movie, ProductAdmin)
admin.site.register(MovieComment)
