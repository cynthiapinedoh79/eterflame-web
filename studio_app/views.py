from django.shortcuts import render


def studio_home(request):
    return render(request, 'studio/home.html', {
        'page_title': 'EF Studio',
        'section': 'studio',
    })
