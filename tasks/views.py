from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("Hola, TaskFlow")