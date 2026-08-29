from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    postes = Poste.objects.filter(is_published=True).order_by('-created_at')[:5]
    context = {}
    context["postes"] = postes
    return render(request, "blog/index.html", context)

def blog(request):
    postes = Poste.objects.filter(is_published=True).order_by('-created_at')
    context = {}
    context["postes"] = postes
    return render(request, "blog/blog.html", context)

def poste(request, slug):
    poste = get_object_or_404(Poste, slug=slug)
    postes = Poste.objects.filter(is_published=True).order_by('-created_at')[:5]
    context = {}
    context["postes"] = postes
    context["poste"] = poste
    return render(request, "blog/poste.html", context)