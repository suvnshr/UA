from django.shortcuts import render
from django.http import HttpResponse
from . import forms as custom_forms

# Create your views here.

def convert(email):

    i = email.index("@")
    first = email[:i]
    last = email[i+1:]
    f = str(idna.encode(first))
    f = f[2:len(f)-1]
    s=str((idna.encode(last)))
    s = s[2:len(s)-1]

    return(f+"@"+s)

def reconvert(email):

    i = email.index("@")
    first = email[:i]
    last = email[i+1:]

    f = str(idna.decode(first))
    s = str((idna.decode(last)))

    return(f+"@"+s)

def index(request):

    form = custom_forms.RegisterForm()

    if request.method == "POST":
        form = custom_forms.RegisterForm(request.POST)

        if form.is_valid():

            return render(request, "main/home.html", {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
            })
        
        else:
            return HttpResponse("Error")

    return render(request, "main/index.html", {
        'form': form
    })

