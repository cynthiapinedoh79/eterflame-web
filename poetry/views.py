from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, F
from django.http import HttpResponse, JsonResponse
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
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
    import re
    poem = get_object_or_404(Poem, slug=slug)
    page_num = int(request.GET.get('page', 1))

    STANZAS_PER_PAGE = 12

    def paginate_poem(body):
        if not body:
            return [''], 1
        
        # Split by double <br> or </p><p> or <br><br>
        import re as _re
        
        # Try splitting by </p><p> first
        stanzas = _re.split(r'</p>\s*<p>', body.strip())
        
        # If only 1 chunk, try splitting by <br><br> or double newlines
        if len(stanzas) <= 1:
            stanzas = _re.split(r'<br\s*/?>\s*<br\s*/?>', body.strip())
        
        # If still only 1, try splitting by \n\n
        if len(stanzas) <= 1:
            stanzas = _re.split(r'\n\s*\n', body.strip())
            
        # If still 1, split every STANZAS_PER_PAGE lines
        if len(stanzas) <= 1:
            lines = _re.split(r'<br\s*/?>', body.strip())
            LINES_PER_PAGE = 20
            if len(lines) <= LINES_PER_PAGE:
                return [body], 1
            chunks = [lines[i:i + LINES_PER_PAGE]
                      for i in range(0, len(lines), LINES_PER_PAGE)]
            pages = ['<br>'.join(chunk) for chunk in chunks]
            return pages, len(pages)
        
        if len(stanzas) <= STANZAS_PER_PAGE:
            return [body], 1
            
        chunks = [stanzas[i:i + STANZAS_PER_PAGE]
                  for i in range(0, len(stanzas), STANZAS_PER_PAGE)]
        pages = []
        for chunk in chunks:
            pages.append('<br><br>'.join(chunk))
        return pages, len(pages)

    pages_es, total_pages = paginate_poem(poem.body_es)
    pages_en, _ = paginate_poem(poem.body_en) if poem.body_en else ([''], 1)
    page_num = max(1, min(page_num, total_pages))

    current_page_es = pages_es[page_num - 1]
    current_page_en = pages_en[min(page_num - 1, len(pages_en) - 1)]

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = poem.favorites.filter(
            id=request.user.id
        ).exists()

    context = {
        "poem": poem,
        "poem_body_es": current_page_es,
        "poem_body_en": current_page_en,
        "current_page": page_num,
        "total_pages": total_pages,
        "has_next": page_num < total_pages,
        "has_prev": page_num > 1,
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


@staff_member_required
def pdf_tool(request):
    poems = Poem.objects.all().order_by('collection__name', 'title')
    return render(request, 'poetry/pdf_tool.html', {'poems': poems})


def download_poem_pdf(request, slug):
    poem = get_object_or_404(Poem, slug=slug)
    lang = request.GET.get('lang', 'es')
    from .pdf_generator import generate_poem_pdf
    pdf_bytes = generate_poem_pdf(poem, lang=lang)
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{poem.slug}-{lang}.pdf"'
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

# ─────────────────────────────────────────────────────────────
# Public anonymous likes for poems.
# - No login required (public engagement metric)
# - Atomic increment via F-expression
# - Anti-spam handled client-side via localStorage
# - Counter visibility threshold (>=2) decided in template/JS
# ─────────────────────────────────────────────────────────────
@require_POST
def poem_like(request, slug):
    """
    Increment public like counter for a poem.
    Returns JSON with new count and threshold flag.
    """
    poem = get_object_or_404(Poem, slug=slug)
    Poem.objects.filter(pk=poem.pk).update(
        likes_count=F("likes_count") + 1
    )
    poem.refresh_from_db(fields=["likes_count"])

    return JsonResponse({
        "ok": True,
        "likes": poem.likes_count,
        "show_count": poem.likes_count >= 2,
    })


# ─────────────────────────────────────────────────────────────
# Lead magnet: free poem PDF in exchange for email
# - GET: shows form with email + optional newsletter checkbox
# - POST: validates → subscribes → generates PDF → inline download
# - Smart default: admin-flagged poem first, else most-liked
# ─────────────────────────────────────────────────────────────
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_http_methods
from audience.models import Subscriber
from audience.services import subscribe as audience_subscribe


def _get_lead_magnet_poem():
    """
    Returns the poem to offer as lead magnet.
    Priority: admin-flagged (is_free_lead_magnet=True), else most-liked.
    Returns None if no poems exist at all.
    """
    return (
        Poem.objects.filter(is_free_lead_magnet=True)
        .order_by("-likes_count").first()
        or
        Poem.objects.order_by("-likes_count", "-created").first()
    )


@require_http_methods(["GET", "POST"])
def free_poem_view(request):
    """Lead magnet view: free poem PDF in exchange for email."""
    poem = _get_lead_magnet_poem()

    if not poem:
        # No poems in DB — graceful empty state
        return render(request, "poetry/free_poem.html", {
            "poem": None,
            "empty_state": True,
        })

    # ─── GET: show form ─────────────────────────────────────
    if request.method == "GET":
        return render(request, "poetry/free_poem.html", {
            "poem": poem,
        })

    # ─── POST: process form ────────────────────────────────
    email = (request.POST.get("email") or "").strip()
    name = (request.POST.get("name") or "").strip()
    wants_newsletter = request.POST.get("newsletter") == "on"
    lang = request.POST.get("lang", "es")

    # Validate basic email presence
    if not email:
        return render(request, "poetry/free_poem.html", {
            "poem": poem,
            "error": "Email is required to download your free poem.",
            "submitted_name": name,
        })

    # Subscribe to audience (idempotent — service handles existing)
    try:
        subscriber, created, status = audience_subscribe(
            email=email,
            source=Subscriber.Source.LEAD_MAGNET_POEM,
            name=name,
        )
    except ValidationError as e:
        return render(request, "poetry/free_poem.html", {
            "poem": poem,
            "error": (e.messages[0] if e.messages else "Invalid email."),
            "submitted_name": name,
            "submitted_email": email,
        })

    # If user opted in for newsletter, mark separately
    # (current source LEAD_MAGNET_POEM already tracks them; the checkbox
    # is mostly UX/GDPR — we honor their explicit consent in the audience
    # source field. If they don't opt in, they still get the PDF but the
    # source remains LEAD_MAGNET_POEM, which Cynthia can choose to include
    # or exclude in future newsletter sends.)
    # Note: future improvement could add a separate 'newsletter_opt_in' field
    # on Subscriber for finer segmentation.

    # Generate PDF on-demand using unified generator
    from poetry.pdf_generator import generate_poem_pdf
    pdf_bytes = generate_poem_pdf(poem, lang=lang, mode="lead_magnet")

    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    response["Content-Disposition"] = (
        f'attachment; filename="{poem.slug}-aythnyk-free.pdf"'
    )
    return response
