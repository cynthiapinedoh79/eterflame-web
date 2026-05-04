from django.db import models
from cloudinary.models import CloudinaryField


class PortfolioItem(models.Model):
    title        = models.CharField(max_length=200)
    kicker       = models.CharField(max_length=100, help_text="e.g. 'Featured Project', 'Web', 'Data · ML'")
    description  = models.TextField()
    image        = CloudinaryField('image', blank=True)
    tags         = models.CharField(max_length=300, blank=True,
                     help_text="Comma-separated e.g. Python,Scikit-learn")
    is_screenshot = models.BooleanField(default=False,
                     help_text="Use contain layout instead of cover (for screenshots/dashboards)")
    order        = models.PositiveIntegerField(default=0)
    is_active    = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def tag_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]
