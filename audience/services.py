"""
Service layer for audience subscriptions.
Encapsulates business logic so views stay thin.
"""
from typing import Optional
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils import timezone

from .models import Subscriber


def subscribe(
    email: str,
    source: str = Subscriber.Source.FOOTER,
    name: str = "",
) -> tuple[Subscriber, bool, str]:
    """
    Subscribe an email to Aythnyk audience.
    
    Idempotent: if email already exists, returns existing subscriber.
    If subscriber was unsubscribed before, re-activates.
    
    Returns:
        (subscriber, created, status)
        - subscriber: the Subscriber instance
        - created: True if new, False if already existed
        - status: 'created' | 'resubscribed' | 'already_subscribed'
    """
    # Normalize email
    email = (email or "").strip().lower()
    name = (name or "").strip()
    
    # Validate
    if not email:
        raise ValidationError("Email es obligatorio.")
    validate_email(email)
    
    # Try to find or create
    subscriber, created = Subscriber.objects.get_or_create(
        email=email,
        defaults={
            "name": name,
            "source": source,
        },
    )
    
    if created:
        return subscriber, True, "created"
    
    # Email already exists — check if previously unsubscribed
    if subscriber.unsubscribed_at is not None:
        subscriber.unsubscribed_at = None
        if name and not subscriber.name:
            subscriber.name = name
        subscriber.save(update_fields=["unsubscribed_at", "name"])
        return subscriber, False, "resubscribed"
    
    return subscriber, False, "already_subscribed"


def unsubscribe_email(email: str) -> Optional[Subscriber]:
    """
    Mark a subscriber as unsubscribed.
    Returns the Subscriber if found, None otherwise.
    """
    email = (email or "").strip().lower()
    try:
        subscriber = Subscriber.objects.get(email=email)
    except Subscriber.DoesNotExist:
        return None
    
    subscriber.unsubscribe()
    return subscriber