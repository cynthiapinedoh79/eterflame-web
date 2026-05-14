"""
Views for audience (newsletter) subscriptions.
Designed to work with AJAX (JSON) and fallback HTML form posts.
"""
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

from .models import Subscriber
from .services import subscribe


SUCCESS_MESSAGES = {
    "created": "You're subscribed. Aythnyk news will arrive soon.",
    "resubscribed": "Welcome back. You'll receive Aythnyk updates again.",
    "already_subscribed": "You're already subscribed to Aythnyk.",
}


@require_POST
@csrf_protect
def subscribe_view(request):
    """
    Handle subscription form POST.
    
    Detects AJAX vs HTML form via Accept header or X-Requested-With.
    Source comes from a hidden 'source' field in the form.
    """
    email = request.POST.get("email", "")
    name = request.POST.get("name", "")
    source = request.POST.get("source", Subscriber.Source.FOOTER)
    
    # Validate source is one of the allowed choices
    valid_sources = {choice[0] for choice in Subscriber.Source.choices}
    if source not in valid_sources:
        source = Subscriber.Source.FOOTER
    
    is_ajax = (
        request.headers.get("X-Requested-With") == "XMLHttpRequest"
        or "application/json" in request.headers.get("Accept", "")
    )
    
    try:
        subscriber, created, status = subscribe(
            email=email,
            source=source,
            name=name,
        )
    except ValidationError as e:
        error_msg = e.messages[0] if e.messages else "Email inválido."
        if is_ajax:
            return JsonResponse(
                {"ok": False, "error": error_msg},
                status=400,
            )
        messages.error(request, error_msg)
        return _redirect_back(request)
    
    success_msg = SUCCESS_MESSAGES.get(status, "Gracias por suscribirte.")
    
    if is_ajax:
        return JsonResponse({
            "ok": True,
            "status": status,
            "message": success_msg,
        })
    
    messages.success(request, success_msg)
    return _redirect_back(request)


def _redirect_back(request):
    """Redirect to referer, or to home if no referer."""
    referer = request.META.get("HTTP_REFERER")
    return redirect(referer or "/")