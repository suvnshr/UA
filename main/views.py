from django.shortcuts import render
from django.http import HttpResponse
from . import forms as custom_forms
from .models import Person

# Create your views here.


def index(request):

    form = custom_forms.RegisterForm()
    is_email_valid = True

    if request.method == "POST":

        form = custom_forms.RegisterForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                person = Person.objects.create(
                    name=name,
                    email=email,
                    password=password,
                )

                person.save()

                return render(request, "main/home.html", {
                    "person": person
                })

            except ValueError:
                is_email_valid = False

        else:
           is_email_valid = False

    return render(request, "main/index.html", {
        "form": form,
        "is_email_valid": is_email_valid,
    })
