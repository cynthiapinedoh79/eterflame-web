from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('print', 'Prints & Art'),
        ('digital', 'Digital Downloads'),
    ]
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='shop/products/', blank=True, null=True)
    external_url = models.URLField(blank=True)
    is_available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-featured', '-created_on']


class CommissionRequest(models.Model):
    OCCASION_CHOICES = [
        ('wedding', 'Wedding'),
        ('birthday', 'Birthday'),
        ('memorial', 'Memorial / Loss'),
        ('dedication', 'Dedication'),
        ('anniversary', 'Anniversary'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField()
    occasion = models.CharField(max_length=20, choices=OCCASION_CHOICES)
    recipient = models.CharField(max_length=200)
    details = models.TextField()
    language = models.CharField(
        max_length=10,
        choices=[('en', 'English'), ('es', 'Español'), ('both', 'Both')],
        default='en',
    )
    budget = models.CharField(max_length=50, blank=True)
    submitted_on = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} — {self.occasion}"

    class Meta:
        ordering = ['-submitted_on']
