from django.contrib import admin
from apps.settings.models import Setting, About, AboutImage
# Register your models here.

class AboutImageAdmin(admin.TabularInline):
    model = AboutImage
    extra = 3

class AboutAdmin(admin.ModelAdmin):
    inlines = [AboutImageAdmin]
    # list_display = ('title', 'genre')
    # search_fields = ('title', 'genre')
    # ordering = ('-genre',)
    # list_per_page = 4
    # prepopulated_fields = {"slug": ('title', )}

admin.site.register(Setting)
admin.site.register(About, AboutAdmin) 
