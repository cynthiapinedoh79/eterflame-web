from django.db import models
from cloudinary.models import CloudinaryField


class AffiliateLink(models.Model):
    CATEGORY_CHOICES = [
        ('dev',       'Development'),
        ('design',    'Design'),
        ('hosting',   'Hosting'),
        ('music',     'Music & Distribution'),
        ('voice',     'Voice & Audio AI'),
        ('video',     'Video & Editing'),
        ('marketing', 'Marketing'),
        ('org',       'Organization'),
    ]
    CHANNEL_CHOICES = [
        ('b2b',     'Etherflame Works only'),
        ('aythnyk', 'Aythnyk only'),
        ('both',    'Both sections'),
    ]

    name          = models.CharField(max_length=100)
    logo          = CloudinaryField('logo', blank=True)
    tagline       = models.CharField(max_length=200,
                      help_text="One line: what it does")
    description   = models.TextField(
                      help_text="2-3 sentences. B2B: professional tone. Aythnyk: personal/creative tone.")
    affiliate_url = models.URLField(help_text="Your affiliate link")
    commission    = models.CharField(max_length=100, blank=True,
                      help_text="e.g. '22% recurrente x 12 meses'")
    category      = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    channel       = models.CharField(max_length=10, choices=CHANNEL_CHOICES,
                      default='both')
    featured      = models.BooleanField(default=False)
    active        = models.BooleanField(default=True)
    order         = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_channel_display()})"
