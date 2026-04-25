from django.shortcuts import render
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
            return render(request, 'shop/commission.html', {
                'form': CommissionForm(),
                'submitted': True,
                'requester_name': obj.name,
            })
    else:
        form = CommissionForm()
    return render(request, 'shop/commission.html', {'form': form, 'submitted': False})
