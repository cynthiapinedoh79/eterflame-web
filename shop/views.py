from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Product
from .forms import CommissionForm


def shop_home(request):
    prints = Product.objects.filter(category='print', is_available=True)
    digital = Product.objects.filter(category='digital', is_available=True)
    return render(request, 'shop/shop_home.html', {'prints': prints, 'digital': digital})


def prints(request):
    products = Product.objects.filter(category='print', is_available=True)
    return render(request, 'shop/prints.html', {'products': products})


def digital(request):
    products = Product.objects.filter(category='digital', is_available=True)
    return render(request, 'shop/digital.html', {'products': products})


def commission(request):
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            obj = form.save()
            _send_commission_email(obj)
            return render(request, 'shop/commission.html', {
                'form': CommissionForm(),
                'submitted': True,
                'requester_name': obj.name,
            })
    else:
        form = CommissionForm()
    return render(request, 'shop/commission.html', {'form': form, 'submitted': False})


def _send_commission_email(obj):
    body = (
        f"New commission request from {obj.name}\n\n"
        f"Email: {obj.email}\n"
        f"Occasion: {obj.get_occasion_display()}\n"
        f"Recipient: {obj.recipient}\n"
        f"Language: {obj.get_language_display()}\n"
        f"Budget: {obj.budget or '—'}\n\n"
        f"Story:\n{obj.details}"
    )
    send_mail(
        subject=f"[Aythnyk] Commission request from {obj.name}",
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=True,
    )
