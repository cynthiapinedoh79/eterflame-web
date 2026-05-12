from django.db import models


class Testimonial(models.Model):
    """Customer testimonial filtered by Eterflame Works division."""
    
    DIVISION_CHOICES = [
        ('design', 'EF Design'),
        ('media',  'EF Media'),
        ('studio', 'EF Studio'),
    ]
    
    RATING_CHOICES = [(i, '★' * i + '☆' * (5 - i)) for i in range(1, 6)]
    
    division        = models.CharField(
                        max_length=10,
                        choices=DIVISION_CHOICES,
                        help_text="Which Eterflame division this testimonial belongs to"
                      )
    quote           = models.TextField(
                        help_text="The testimonial text (will appear in quotes)"
                      )
    author_name     = models.CharField(max_length=100)
    author_role     = models.CharField(
                        max_length=200,
                        help_text="e.g. 'Founder, Acme Corp' or 'Marketing Director'"
                      )
    author_company  = models.CharField(max_length=200, blank=True)
    rating          = models.PositiveSmallIntegerField(
                        default=5,
                        choices=RATING_CHOICES
                      )
    is_featured     = models.BooleanField(
                        default=False,
                        help_text="Highlight this testimonial in division page"
                      )
    is_active       = models.BooleanField(default=True)
    order           = models.PositiveIntegerField(
                        default=0,
                        help_text="Lower = first. Same order = newest first."
                      )
    created_at      = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
    
    def __str__(self):
        return f"{self.author_name} — {self.get_division_display()}"
    
    @property
    def stars(self):
        """Returns the star representation for templates."""
        return '★' * self.rating + '☆' * (5 - self.rating)
