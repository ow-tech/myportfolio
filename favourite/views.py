from django.shortcuts import render



def home(request):
    title ="Home"
    return render( request,"all-projects/home.html",{"title":title,})

def about(request):
    title ="About"
    return render( request,"all-projects/about.html",{"title":title,})