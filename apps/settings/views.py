from django.shortcuts import render
from apps.settings.models import Setting
# Create your views here.

def index(request):
    return render(request, 'index.html' )
