from django.shortcuts import render


# Create your views here.
def index(request):
    title ="list"
    return render( request,"all-projects/list.html",{"title":title,})