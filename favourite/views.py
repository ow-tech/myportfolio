from django.shortcuts import render, get_object_or_404
from .models import Project_disc, Projects
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import ContactForm
from django.http import HttpResponse


def home(request):
    title ="Home"
    projects = Projects.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['alexbarasa0723@gmail.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=False)
            except BadHeaderError:
                return HttpResponse ('Invalid Header Found')
            return HttpResponse('Success... Your Email Sent')
    context = {
        'projects':projects,
        'titile':title,
        'form':form,
    }
    return render( request,"all-projects/home.html", context)

def about(request):
    title ="About"

    return render( request,"all-projects/home.html",{"title":title,})

def portfolio(request):
    projects = Projects.objects.all()
    context = {
        'projects':projects,
        'titile':portfolio
    }
    title ="Portfolio"
    return render (request, 'all-projects/home.html', context)

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
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['alexbarasa0723@gmail.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=False)
            except BadHeaderError:
                return HttpResponse ('Invalid Header Found')
            return HttpResponse('Success... Your Email Sent')
    return render (request, 'all-projects/home.html', {'form':form})