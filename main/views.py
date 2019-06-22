from django.shortcuts import render
from django.http import HttpResponse
import idna
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
    return render(request, "main/index.html")

