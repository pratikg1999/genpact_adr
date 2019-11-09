from django.shortcuts import render, redirect
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
            name = pres_form.cleaned_data['name']
            age = pres_form.cleaned_data['age']
            gender = pres_form.cleaned_data['gender']
            disease = pres_form.cleaned_data['disease']
            medication = pres_form.cleaned_data['medication']
            pres_obj = models.Prescription(name = 'anurag', age = 1, gender = 1, disease = 'afnjkhi', medication="medication")
            pres_obj.save()

            # do the prediction and searching stuff here, the prediction results has to be rendered with results.html

            if naranjoFieldValue == -1:
                # do the data saving due to naranjoField here.
                random_code_to_fill_if_statement = 1
            return render(request, 'adr/result.html', {'isADR': False})
        else:
            return HttpResponse("Something went wrong")


    return render(request, 'adr/home.html', {})

def reverseSave(reverse):
    models.Prescription.objects.latest('id').delete()
    return redirect(home)

