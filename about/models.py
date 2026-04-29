from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class About(models.Model):
    """
    Stores a single about / collaborator profile.
    """

    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    # Credentials / profile highlights
    credential_title = models.CharField(
        max_length=200,
        blank=True,
        default="Core Expertise"
    )
    credential_subtitle = models.CharField(
        max_length=250,
        blank=True,
        default="Skills · Focus Areas · Technical Direction"
    )
    credential_summary = models.TextField(
        blank=True,
        default="A curated overview of this profile’s strongest technical, creative, and strategic capabilities."
    )
    skills = models.CharField(
        max_length=500,
        blank=True,
        help_text="Separate skills with commas. Example: Python, Django, JavaScript, PostgreSQL"
    )

    focus_1_title = models.CharField(max_length=100, blank=True, default="Frontend")
    focus_1_text = models.CharField(
        max_length=250,
        blank=True,
        default="Responsive layouts, UI systems, and user experience foundations."
    )

    focus_2_title = models.CharField(max_length=100, blank=True, default="Backend")
    focus_2_text = models.CharField(
        max_length=250,
        blank=True,
        default="Django architecture, databases, APIs, and scalable web logic."
    )

    focus_3_title = models.CharField(max_length=100, blank=True, default="Data")
    focus_3_text = models.CharField(
        max_length=250,
        blank=True,
        default="Analytics, visualisation, and machine learning workflows."
    )

    @property
    def skills_as_list(self):
        """
        Returns skills as a clean list from comma-separated text.
        """
        if not self.skills:
            return []
        return [skill.strip() for skill in self.skills.split(",") if skill.strip()]

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Stores a collaboration request from a user.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
