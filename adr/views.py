from django.shortcuts import render
from django.http import HttpResponse


def naranjo(request):
    context = {"title": "Naranjo"}
    return render(request, 'adr/naranjo.html', context)

def home(request):

    return render(request, 'adr/home.html', {})