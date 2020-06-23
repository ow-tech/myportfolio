from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    # path('about', views.about, name='about'),
    # path('portfolio', views.portfolio, name='portfolio'),
    path('(<int:id>)/', views.details, name='details'),
    # path('contact', views.contact, name='contact'),
]