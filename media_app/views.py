from django.shortcuts import render


def media_home(request):
    return render(request, 'media/home.html', {
        'page_title': 'EF Media',
        'section': 'media',
    })
