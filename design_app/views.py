from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator

from .models import PortfolioItem, CaseStudy


def design_home(request):
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

    items = PortfolioItem.objects.filter(is_active=True).order_by('order')
    
    # Separate featured project from regular items
    featured = items.filter(is_featured=True).first()
    if featured:
        regular_items = items.exclude(id=featured.id)
    else:
        regular_items = items
    
    paginator = Paginator(regular_items, 6)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'design/home.html', {
        'page_title': 'EF Design',
        'section': 'design',
        'featured': featured,
        'page_obj': page_obj,
    })


def case_study_conversion(request):
    return render(request, 'design/case_study_conversion.html', {
        'page_title': 'Case Study — Digital Marketing Conversion Predictor',
        'section': 'design',
    })


def case_study_detail(request, slug):
    case_study = get_object_or_404(CaseStudy, slug=slug, is_published=True)
    return render(request, 'design/case_study_detail.html', {
        'cs': case_study,
        'page_title': f'Case Study — {case_study.portfolio_item.title}',
        'section': 'design',
    })
