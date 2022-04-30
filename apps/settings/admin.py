from django.contrib import admin
from apps.settings.models import Setting, About
# Register your models here.
admin.site.register(Setting)
admin.site.register(About)