from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import Poem, Collection, Author
from songs.models import Song
from works.models import AffiliateLink


def _build_poem_list_context(request):
    """
    Builds the context for the poem/collection list pages.
    Allows stacking filters such as search, collection, and author.
    """
    q = (request.GET.get("q") or "").strip()
    page_number = request.GET.get("page")
    collection_slug = request.GET.get("collection")
    author_slug = request.GET.get("author")

    all_collections = Collection.objects.all().order_by("name_en")
    all_authors = Author.objects.all().order_by("name")

    current_collection = None
    current_author = None

    favorite_poem_ids = []
    if request.user.is_authenticated:
        favorite_poem_ids = request.user.favorite_poems.values_list(
            "id",
            flat=True
        )

    page_mode = "poems"
    qs = Poem.objects.all().order_by("-is_featured", "-created")

    if q:
        qs = qs.filter(
            Q(title_es__icontains=q)
            | Q(title_en__icontains=q)
            | Q(body_es__icontains=q)
            | Q(body_en__icontains=q)
            | Q(author__name__icontains=q)
        )

    if collection_slug and collection_slug != "all-poems":
        try:
            current_collection = Collection.objects.get(
                slug=collection_slug
            )
            qs = qs.filter(collection=current_collection)
        except Collection.DoesNotExist:
            qs = Poem.objects.none()

    if author_slug:
        try:
            current_author = Author.objects.get(slug=author_slug)
            qs = qs.filter(author=current_author)
        except Author.DoesNotExist:
            qs = Poem.objects.none()

    if not q and not collection_slug and not author_slug:
        page_mode = "collections"
        qs = Collection.objects.all().order_by("name_en")

    total = qs.count()
    paginator = Paginator(qs, 12)
    page_obj = paginator.get_page(page_number)

    return {
        "page_obj": page_obj,
        "page_mode": page_mode,
        "q": q,
        "total": total,
        "all_collections": all_collections,
        "all_authors": all_authors,
        "current_collection_slug": collection_slug,
        "current_collection": current_collection,
        "current_author_slug": author_slug,
        "current_author": current_author,
        "favorite_poem_ids": favorite_poem_ids,
        "series_list": Song.SERIES_CHOICES,
    }


def poem_detail(request, slug):
    """Display a single poem's detail page."""
    poem = get_object_or_404(Poem, slug=slug)

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = poem.favorites.filter(
            id=request.user.id
        ).exists()

    context = {
        "poem": poem,
        "is_favorite": is_favorite,
        "related_songs": poem.songs.filter(active=True),
    }
    return render(request, "poetry/poem_detail.html", context)


def poem_list(request):
    """Display a list of poems or collections based on filters."""
    import logging
    logger = logging.getLogger(__name__)
    try:
        ctx = _build_poem_list_context(request)
        return render(request, "poetry/poem_list.html", ctx)
    except Exception as e:
        logger.error(f"poem_list error: {e}")
        ctx = {
            "page_obj": None,
            "page_mode": "collections",
            "q": "",
            "total": 0,
            "all_collections": [],
            "all_authors": [],
            "current_collection_slug": None,
            "current_collection": None,
            "current_author_slug": None,
            "current_author": None,
            "favorite_poem_ids": [],
        }
        return render(request, "poetry/poem_list.html", ctx)


def poetry_home(request):
    """Display the poetry home page with hero image and quotes."""
    quotes = [
        {
            "text": "Feel the paper with the breathings of your heart",
            "author": "William Wordsworth",
        },
        {
            "text": "Creativity involves breaking out of established"
            "patterns...",
            "author": "Edward de Bono",
        },
        {
            "text": "Poetry is a spontaneous overflow of powerful feelings.",
            "author": "William Wordsworth",
        },
        {
            "text": "The chief enemy of creativity is good sense.",
            "author": "Pablo Picasso",
        },
        {
            "text": "Be yourself; everyone else is already taken.",
            "author": "Oscar Wilde",
        },
        {
            "text": "True poems are fires that burn and shine.",
            "author": "Vicente Huidobro",
        },
        {
            "text": "Poetry is the language of the soul.",
            "author": "Unknown",
        },
        {
            "text": (
                "To try to express with words what the soul feels would "
                "be like trying to trap the sea’s water in a container."
            ),
            "author": "Marta Martín Girón",
        },
    ]

    try:
        all_collections = Collection.objects.all().order_by("name_en")
    except Exception:
        all_collections = []

    ctx = {
        "hero_image_url": static("images/poetry_hero.png"),
        "cover_image_url": static("images/poetry_cover.png"),
        "quotes": quotes,
        "all_collections": all_collections,
        "hide_page_title": True,
    }
    return render(request, "poetry/home.html", ctx)


@login_required
@require_POST
def toggle_favorite(request, poem_id):
    """Toggle a poem as a favorite for the logged-in user."""
    poem = get_object_or_404(Poem, id=poem_id)

    is_favorited = poem.favorites.filter(
        id=request.user.id
    ).exists()

    if is_favorited:
        poem.favorites.remove(request.user)
        messages.info(
            request,
            f"'{poem.title_en}' has been removed from your favorites."
        )
    else:
        poem.favorites.add(request.user)
        messages.success(
            request,
            f"'{poem.title_en}' has been added to your favorites! ❤️"
        )

    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "aythnyk:aythnyk_home"
        )
    )


@login_required
def favorites_list(request):
    """Display the logged-in user's favorite poems."""
    favorite_poems = request.user.favorite_poems.all().order_by(
        "-is_featured",
        "-created",
    )

    ctx = _build_poem_list_context(request)

    paginator = Paginator(favorite_poems, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    ctx.update(
        {
            "page_obj": page_obj,
            "page_mode": "poems",
            "total": favorite_poems.count(),
            "is_favorites_page": True,
        }
    )

    return render(request, "poetry/poem_list.html", ctx)


def author_detail(request, slug):
    """Display an author's bio and a list of their poems."""
    author = get_object_or_404(Author, slug=slug)

    poems = Poem.objects.filter(author=author).order_by(
        "-is_featured",
        "-created",
    )

    paginator = Paginator(poems, 18)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    favorite_poem_ids = []
    if request.user.is_authenticated:
        favorite_poem_ids = request.user.favorite_poems.values_list(
            "id",
            flat=True,
        )

    context = {
        "author": author,
        "page_obj": page_obj,
        "favorite_poem_ids": favorite_poem_ids,
    }
    return render(request, "poetry/author_detail.html", context)


def download_poem_pdf(request, slug):
    poem = get_object_or_404(Poem, slug=slug)
    from .pdf_generator import generate_poem_pdf
    pdf_bytes = generate_poem_pdf(poem)
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{poem.slug}.pdf"'
    return response


def aythnyk_tools(request):
    links = AffiliateLink.objects.filter(
        active=True,
        channel__in=['aythnyk', 'both']
    )
    categories = {}
    for link in links:
        cat = link.get_category_display()
        categories.setdefault(cat, []).append(link)
    return render(request, 'poetry/tools.html', {
        'categories': categories,
        'featured': links.filter(featured=True),
    })
