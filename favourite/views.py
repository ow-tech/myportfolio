from django.shortcuts import render
from .models import Project_disc, Projects


def home(request):
    title ="Home"
    return render( request,"all-projects/home.html",{"title":title,})

def about(request):
    title ="About"
    return render( request,"all-projects/about.html",{"title":title,})

def portfolio(request):
    projects = Projects.objects.all()
    title ="Portfolio"
    return render (request, 'all-projects/portfolio.html', {'title':title})