from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import About
from .forms import CollaborateForm
from django.core.mail import send_mail
from django.conf import settings


def about_me(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration requests.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
        ``collaborate_form``
            An instance of :form:`about.CollaborateForm`.

    **Template**
    :template:`about/about.html`
    """
    # 1. Always fetch the static content
    try:
        about = About.objects.all().order_by('-updated_on').last()
    except Exception:
        about = None

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            
            send_mail(
                subject=f"[AYTHNYK] New collaboration request from {collaborate_form.cleaned_data['name']}",
                message=(
                    f"Name: {collaborate_form.cleaned_data['name']}\n"
                    f"Email: {collaborate_form.cleaned_data['email']}\n\n"
                    f"Message:\n{collaborate_form.cleaned_data['message']}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            messages.add_message(
                request,
                messages.SUCCESS,
                "Collaboration request received!"
                "I endeavour to respond within 2 working day."
            )

            # CRITICAL FIX: Manually save session to ensure messages persist
            request.session.save()

            return redirect(reverse('about'))

    # 2. Handle GET request or unsuccessful POST
    else:
        # This block handles the initial GET and the GET following the redirect
        collaborate_form = CollaborateForm()

    # 3. Final render path (only for GET or invalid POST)
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )


def profile_list(request):
    """
    NEW FUNCTION: Renders a list of all available About profiles.

    FIX: The template path is simplified to resolve
    TemplateDoesNotExist errors.
    Since you have the file in
    'about/templates/about/profile_list.html',
    we simplify the request to "profile_list.html" to force Django to find it
    within the app's template directory structure.
    """
    # Fetch all profiles and order them by title for easy reading
    try:
        profiles = About.objects.all().order_by('title')
    except Exception:
        profiles = []

    return render(
        request,
        "about/profile_list.html",  # <-- FINAL TEMPLATE PATH FIX
        {
            "profiles": profiles
        }
    )


def profile_detail(request, profile_title):
    """
    Renders a specific profile instance based on its title.

    CRITICAL FIX: Removed all form handling.
    The form will be hidden by the template.
    """
    # IMPORTANT: Fetch the profile using the unique 'title' string.
    about = get_object_or_404(About, title__iexact=profile_title)

    # Simple redirect on POST to prevent crashes if a form somehow appears
    if request.method == "POST":
        return redirect(reverse('about'))

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            # collaborate_form is explicitly NOT passed here,
            # separating it from this view
        },
    )
