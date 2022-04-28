from django.contrib import admin
from apps.users.models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # fields = ('username', 'tel') #output data
    # exclude = ('username', ) # Field's exceptions
    list_display = ('username', 'email', 'tel')
    search_fields = ('username', 'email')
    ordering = ('username',)
    list_per_page = 1

admin.site.register(User, UserAdmin)