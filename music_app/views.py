from django.shortcuts import render


def music_home(request):
    return render(request, 'music/home.html', {
        'page_title': 'EF Music',
        'section': 'music',
    })
