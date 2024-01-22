from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page1", views.index, name="index"),
    path("apply_ville", views.index2, name="index")
]