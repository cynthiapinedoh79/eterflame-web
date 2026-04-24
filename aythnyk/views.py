from django.shortcuts import render
from django.templatetags.static import static
from poetry.models import Collection


def aythnyk_home(request):
    quotes = [
        {"text": "Feel the paper with the breathings of your heart",
         "author": "William Wordsworth"},
        {"text": "Poetry is a spontaneous overflow of powerful feelings.",
         "author": "William Wordsworth"},
        {"text": "The chief enemy of creativity is good sense.",
         "author": "Pablo Picasso"},
        {"text": "Be yourself; everyone else is already taken.",
         "author": "Oscar Wilde"},
        {"text": "True poems are fires that burn and shine.",
         "author": "Vicente Huidobro"},
    ]

    try:
        all_collections = Collection.objects.all().order_by("name_en")
    except Exception:
        all_collections = []

    ctx = {
        "hero_image_url": static("images/poetry_hero.png"),
        "quotes": quotes,
        "all_collections": all_collections,
        "hide_page_title": True,
    }
    return render(request, "aythnyk/home.html", ctx)
