"""
Template tags for displaying testimonials in templates.

Usage in any template:
    {% load testimonial_tags %}
    {% show_testimonials 'design' %}
"""
from django import template
from testimonials.models import Testimonial

register = template.Library()


@register.inclusion_tag('components/testimonials_section.html')
def show_testimonials(division, limit=6):
    """
    Renders testimonials section for a specific division.
    
    Args:
        division: 'design', 'media', or 'studio'
        limit: max number of testimonials to show (default 6)
    
    Featured testimonials appear first, then by order.
    Only active testimonials are shown.
    """
    testimonials = Testimonial.objects.filter(
        division=division,
        is_active=True
    ).order_by('-is_featured', 'order')[:limit]
    
    return {
        'testimonials': testimonials,
        'division': division,
    }
