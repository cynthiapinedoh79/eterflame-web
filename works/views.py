from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from .models import AffiliateLink


def works_home(request):
    return render(request, 'works/home.html')


def resources(request):
    links = AffiliateLink.objects.filter(
        active=True,
        channel__in=['b2b', 'both']
    )
    categories = {}
    for link in links:
        cat = link.get_category_display()
        categories.setdefault(cat, []).append(link)
    return render(request, 'works/resources.html', {
        'categories': categories,
        'featured': links.filter(featured=True),
    })


def design(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        service = request.POST.get('service', '').strip()
        description = request.POST.get('description', '').strip()
        budget = request.POST.get('budget', '').strip()
        timeline = request.POST.get('timeline', '').strip()

        if name and email and description:
            body = (
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Service: {service}\n"
                f"Budget: {budget}\n"
                f"Timeline: {timeline}\n\n"
                f"Message:\n{description}"
            )
            send_mail(
                subject=f"[EF Design] New enquiry from {name}",
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent. We'll be in touch soon.")
            return redirect('works:design')
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'works/design.html')


def media(request):
    return render(request, 'works/media.html')


def studio(request):
    return render(request, 'works/studio.html')
