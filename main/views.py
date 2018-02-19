from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    #return HttpResponse("<h2>Hello, world. You're at the main index.</h2>")
    return render(request, 'main/home.html')
