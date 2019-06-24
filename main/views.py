from django.shortcuts import render
from django.http import HttpResponse
from . import forms as custom_forms
from .models import Person

# Create your views here.


def index(request):

    error = False
    p = None
    form = custom_forms.RegisterForm()

    if request.method == "POST":
        form = custom_forms.RegisterForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                p = Person.objects.create(name=name, email=email, password=password)
                p.save()

            except ValueError:
                error = True

            if not error:
                return render(request, "main/home.html", {"person": p})

        else:
            return HttpResponse("Error")

    return render(request, "main/index.html", {"form": form, "error": error})

