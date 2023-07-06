from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("contacto/", views.contacto, name="contacto"),
    path("costeo/", views.costeo, name="costeo"),
    path("recetas/", views.recetas, name="recetas"),


]