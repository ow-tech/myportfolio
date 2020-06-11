from django.shortcuts import render


# Create your views here.
def home(request):
    title ="list"
    return render( request,"all-projects/home.html",{"title":title,})