from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import folium
dat = pd.read_csv("valeursfoncieres-2023.txt", sep='|', low_memory=False)

def index(request):

    context = {
        
    }
    return render(request,"accueil.html", context)

def Choix(request):

    context = {
        
    }
    return render(request,"Choix.html", context)

def choix_abs(request):

    context = {
        
    }
    return render(request,"choix_abs.html", context)

def choix_ord(request):
    valeur=request.GET["valeur"]
    context = {
        'valeur' : valeur
    }
    return render(request,"choix_ord.html", context)

def Paris() :
    data = dat[dat["Commune"].str.startswith("PARIS ")]
    data = data.groupby("Commune").size().reset_index(name="Nombre de ventes")
    fig = px.bar(data, x="Commune", y="Nombre de ventes")
    plot_html = fig.to_html(full_html = False, default_height=500, default_width=700)
    return plot_html

def Marseille() :
    data = dat[dat["Commune"].str.startswith("MARSEILLE ")]
    data = data[data["Commune"].str.endswith("ME")]
    data = data.groupby("Commune").size().reset_index(name="Nombre de ventes")
    fig = px.bar(data, x="Commune", y="Nombre de ventes")
    plot_html = fig.to_html(full_html = False, default_height=500, default_width=700)
    return plot_html

def Lyon() :
    data = dat[dat["Commune"].str.startswith("LYON ")]
    data = data.groupby("Commune").size().reset_index(name="Nombre de ventes")
    fig = px.bar(data, x="Commune", y="Nombre de ventes")
    plot_html = fig.to_html(full_html = False, default_height=500, default_width=700)
    return plot_html

def plot(abscisse, ordonnee):
    abscisse = str(abscisse)
    ordonnee = str(ordonnee)
    data = dat.groupby(abscisse)[ordonnee].mean().reset_index()
    fig = px.bar(data, x=abscisse, y=ordonnee)
    plot_html = fig.to_html(full_html = False, default_height=500, default_width=700)
    return plot_html




def index2(request):

    template = loader.get_template('template.html')
    if request.GET["ville"]=="PARIS":
        plot_html = Paris()
    if request.GET["ville"]=="MARSEILLE":
        plot_html = Marseille()
    if request.GET["ville"]=="LYON" :
        plot_html = Lyon()
    context = {
        "plot_html" : plot_html
    }
    return HttpResponse(template.render(context, request))

def print_plot(request):
    template = loader.get_template('plot.html')
    absc = request.GET.get("valeur")
    ord = request.GET.get("valeur2")
    #plot_html = plot(absc, ord)
    context = {
        #"plot_html" : plot_html
        'absc' : absc,
        "ord" : ord
        
    }
    return HttpResponse(template.render(context, request))

