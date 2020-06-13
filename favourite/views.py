from django.shortcuts import render, get_object_or_404
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

def details(request, id):
    projects = get_object_or_404(Projects, id=id)
    project_disc = Project_disc.objects.filter(projects=projects)
    context = {
        "projects":projects,
        "project_disc":project_disc,
        "title":detail
    }
    return render (request, 'all-projects/detail.html', context)