from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.utils.text import slugify  # <-- NEW: Import slugify
from django.contrib.auth.models import User  # <-- NEW: Import the User model


class Author(models.Model):
    """Model representing an author"""
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    bio_en = models.TextField(blank=True)
    bio_es = models.TextField(blank=True)
    # photo = models.ImageField(upload_to="authors/", blank=True, null=True)
    photo = CloudinaryField('author_photo', default='placeholder_author', blank=True, null=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    """Model representing a collection of poems"""
    name_en = models.CharField(max_length=120)
    name_es = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    description_en = models.TextField(blank=True)
    description_es = models.TextField(blank=True)

    # --- NEW: Add this line for the collection image ---
    collection_image = CloudinaryField(
        'collection_image', default='placeholder', blank=True, null=True
    )

    def __str__(self):
        return self.name_es or self.name_en

    def save(self, *args, **kwargs):
        if not self.slug:
            name_to_slugify = self.name_en or self.name_es
            self.slug = slugify(name_to_slugify)
        super().save(*args, **kwargs)


class Poem(models.Model):
    """Model representing a poem"""
    title_en = models.CharField(max_length=200)
    title_es = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    collection = models.ForeignKey(
        Collection, on_delete=models.SET_NULL, null=True, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    body_en = models.TextField()
    body_es = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # --- NEW: Add this line for favorites ---
    favorites = models.ManyToManyField(
        User, related_name='favorite_poems', blank=True)
    # ----------------------------------------

    # Public likes (anonymous, no login required, browser-tracked via localStorage)
    likes_count = models.PositiveIntegerField(
        default=0,
        help_text="Public anonymous likes (global counter, browser anti-spam)"
    )

    # --- Lead magnet: free PDF download ---
    is_free_lead_magnet = models.BooleanField(
        default=False,
        help_text=(
            "When True, this poem is offered as free downloadable PDF "
            "in exchange for email at /aythnyk/free-poem/. "
            "If multiple poems are marked, the most-liked is shown first."
        ),
    )

    def __str__(self):
        return self.title_es or self.title_en

    @property
    def title(self):     # convenience for templates
        return self.title_en or self.title_es

    @property
    def body(self):      # convenience for templates
        return self.body_es or self.body_en

    def get_absolute_url(self):
        return reverse('poetry:poem_detail', args=[self.slug])
