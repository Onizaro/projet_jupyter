from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="accueil"),
    path("choix", views.Choix, name="Choix"),
    path("apply_ville", views.index2, name="plot1"),
    path("choix_abs", views.choix_abs, name="choix1"),
    path("abscisse", views.choix_ord, name="choix2"),
    path("ordonnee", views.print_plot, name="plot")

]