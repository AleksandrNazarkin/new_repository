from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('price', views.price, name='price'),
    ]
#    path('price', views.price),
#    path('catalog', views.catalog)