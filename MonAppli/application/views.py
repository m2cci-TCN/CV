from django.shortcuts import render

# Create your views here.


def acceuil(request):
    return render(request, "acceuil.html")

def competences(request):
    return render(request, "compétences.html")

def contact(request):
    return render(request, "contact.html")

def formations(request):
    return render(request, "formations.html")

def experiences(request):
    return render(request, "experiences.html")

