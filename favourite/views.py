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
    context = {
        'projects':projects,
        'titile':portfolio
    }
    title ="Portfolio"
    return render (request, 'all-projects/portfolio.html', context)

def details(request, id):
    projects = get_object_or_404(Projects, id=id)
    print (projects)
    project_disc = Project_disc.objects.filter(projects=projects)
    title ="details"
    context = {
        "projects":projects,
        "project_disc":project_disc,
        "title":title
    }
    return render (request, 'all-projects/details.html', {"project_disc":project_disc, "title":title, "projects":projects})

def contact(request):
    projects = Projects.objects.all()
    title ="Portfolio"
    return render (request, 'all-projects/portfolio.html', {'title':title})