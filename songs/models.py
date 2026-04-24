from django.db import models
from cloudinary.models import CloudinaryField


class Song(models.Model):
    SERIES_CHOICES = [
        ('emotional', 'Emotional Series'),
        ('lyric',     'Lyric Series'),
        ('dramatic',  'Dramatic Series'),
        ('cinematic', 'Cinematic Series'),
    ]
    title           = models.CharField(max_length=200)
    slug            = models.SlugField(unique=True)
    lyrics          = models.TextField(blank=True)
    poem            = models.ForeignKey(
                        'poetry.Poem',
                        null=True, blank=True,
                        on_delete=models.SET_NULL,
                        related_name='songs'
                      )
    series          = models.CharField(max_length=20, choices=SERIES_CHOICES)
    suno_url        = models.URLField(blank=True, help_text="Internal use only — not shown publicly")
    spotify_url     = models.URLField(blank=True)
    apple_music_url = models.URLField(blank=True)
    pandora_url     = models.URLField(blank=True)
    youtube_music_url = models.URLField(blank=True)
    youtube_url     = models.URLField(
                        blank=True,
                        help_text="YouTube video URL (poem image + voice + music) — shown on page"
                      )
    instagram_url   = models.URLField(blank=True, help_text="Instagram reel URL")
    instagram_thumbnail = CloudinaryField(
                        'instagram_thumb', blank=True,
                        help_text="Instagram reel thumbnail"
                      )
    tiktok_url      = models.URLField(blank=True, help_text="TikTok hook URL")
    tiktok_thumbnail = CloudinaryField(
                        'tiktok_thumb', blank=True,
                        help_text="TikTok hook thumbnail"
                      )
    facebook_url    = models.URLField(blank=True, help_text="Facebook reel URL")
    facebook_thumbnail = CloudinaryField(
                        'facebook_thumb', blank=True,
                        help_text="Facebook reel thumbnail"
                      )
    cover_image     = CloudinaryField('image', blank=True)
    pdf_price       = models.DecimalField(max_digits=6, decimal_places=2,
                        null=True, blank=True,
                        help_text="Price in USD for PDF download")
    pdf_buy_url     = models.URLField(blank=True,
                        help_text="Payment link (Gumroad, Stripe, etc)")
    created_on      = models.DateTimeField(auto_now_add=True)
    active          = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('songs:song_detail', kwargs={'slug': self.slug})
