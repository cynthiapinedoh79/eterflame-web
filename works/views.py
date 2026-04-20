from django.shortcuts import render


def works_home(request):
    return render(request, "works/home.html")


def design(request):
    return render(request, "works/design.html")


def media(request):
    return render(request, "works/media.html")


def studio(request):
    return render(request, "works/studio.html")
