from django.shortcuts import render
from django.http import HttpResponse
from . import models, forms

def naranjo(request):
    context = {"title": "Naranjo"}
    return render(request, 'adr/naranjo.html', context)

def home(request):
    if request.method == 'POST':
        pres_form = forms.prescription_form(request.POST or None)

        if (pres_form.is_valid()):
            naranjoFieldValue = pres_form.cleaned_data['naranjoFieldValue']
            return HttpResponse(naranjoFieldValue)
        else:
            return HttpResponse("Something went wrong")


    return render(request, 'adr/home.html', {})