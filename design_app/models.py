from django.db import models
from django.utils.text import slugify


class PortfolioItem(models.Model):
    title        = models.CharField(max_length=200)
    kicker       = models.CharField(max_length=100, help_text="e.g. 'Featured Project', 'Web', 'Data · ML'")
    description  = models.TextField()
    image_url    = models.URLField(
                     blank=True,
                     default='',
                     help_text="Paste the full Cloudinary URL or any image URL"
                   )
    tags         = models.CharField(max_length=300, blank=True,
                     help_text="Comma-separated e.g. Python,Scikit-learn")
    is_screenshot = models.BooleanField(default=False,
                     help_text="Use contain layout instead of cover (for screenshots/dashboards)")
    is_featured  = models.BooleanField(default=False,
                     help_text="Highlight this project as the main featured work (renders full-width)")
    order        = models.PositiveIntegerField(default=0)
    is_active    = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        """Ensure only ONE featured project exists at a time."""
        if self.is_featured:
            # When marking this as featured, unmark all others
            PortfolioItem.objects.exclude(pk=self.pk).update(is_featured=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def tag_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]


class CaseStudy(models.Model):
    portfolio_item = models.OneToOneField(
        PortfolioItem,
        on_delete=models.CASCADE,
        related_name='case_study',
        null=True, blank=True
    )
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    title_line1 = models.CharField(max_length=200, blank=True,
        help_text="First line of hero title e.g. 'Digital Marketing'")
    title_line2 = models.CharField(max_length=200, blank=True,
        help_text="Second line in italic cyan e.g. 'Conversion Predictor'")
    eyebrow = models.CharField(max_length=200, default='Case Study',
        help_text="e.g. 'Data · ML · Case Study'")
    subtitle = models.CharField(max_length=300, blank=True)
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    # Metrics (up to 5)
    metric_1_value = models.CharField(max_length=50, blank=True)
    metric_1_label = models.CharField(max_length=100, blank=True)
    metric_2_value = models.CharField(max_length=50, blank=True)
    metric_2_label = models.CharField(max_length=100, blank=True)
    metric_3_value = models.CharField(max_length=50, blank=True)
    metric_3_label = models.CharField(max_length=100, blank=True)
    metric_4_value = models.CharField(max_length=50, blank=True)
    metric_4_label = models.CharField(max_length=100, blank=True)
    metric_5_value = models.CharField(max_length=50, blank=True)
    metric_5_label = models.CharField(max_length=100, blank=True)

    # Content blocks
    challenge = models.TextField(blank=True)
    approach = models.TextField(blank=True)
    approach_bullets = models.TextField(blank=True,
        help_text="One bullet per line")
    approach_insight = models.TextField(blank=True,
        help_text="Highlighted insight block")
    deliverables = models.TextField(blank=True,
        help_text="One bullet per line")
    results_intro = models.TextField(blank=True)
    results_outro = models.TextField(blank=True)
    result_1_desc = models.CharField(max_length=200, blank=True,
        help_text="e.g. 'Exceeded target of ≥ 0.80'")
    result_2_desc = models.CharField(max_length=200, blank=True)
    result_3_desc = models.CharField(max_length=200, blank=True)

    # CTA
    cta_title = models.CharField(max_length=200,
        default="Let's turn your data into direction.")

    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Case Study'
        verbose_name_plural = 'Case Studies'

    def __str__(self):
        return self.portfolio_item.title if self.portfolio_item else self.slug

    def save(self, *args, **kwargs):
        if not self.slug and self.portfolio_item:
            self.slug = slugify(self.portfolio_item.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('design:case_study_detail', kwargs={'slug': self.slug})
    
    def get_metrics(self):
        metrics = []
        for i in range(1, 6):
            val = getattr(self, f'metric_{i}_value')
            label = getattr(self, f'metric_{i}_label')
            if val and label:
                metrics.append({'value': val, 'label': label})
        return metrics

    def get_result_cards(self):
        cards = []
        for i in range(1, 4):
            val = getattr(self, f'metric_{i}_value')
            label = getattr(self, f'metric_{i}_label')
            desc = getattr(self, f'result_{i}_desc')
            if val and label:
                cards.append({'value': val, 'label': label, 'desc': desc})
        return cards

    def get_approach_bullets(self):
        return [b.strip() for b in self.approach_bullets.split('\n') if b.strip()]

    def get_deliverables(self):
        return [d.strip() for d in self.deliverables.split('\n') if d.strip()]
