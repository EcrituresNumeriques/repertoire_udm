from django.contrib.auth import logout
from django.shortcuts import render, redirect
from repertoire import models

def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    oeuvres = models.Oeuvre.objects.all()

    return render(request, 'core/home.html',
        { 'oeuvres': oeuvres }
    )
