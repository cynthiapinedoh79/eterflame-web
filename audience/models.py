from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    """
    Suscriptor a contenido de Aythnyk.
    Transversal a poetry, blog, sonic, shop, tools.
    """

    class Source(models.TextChoices):
        FOOTER = "footer", "Footer (todas las páginas)"
        AYTHNYK_SECTION = "aythnyk_section", "Sección /aythnyk/"
        BLOG = "blog", "Form del blog"
        USER_OPTIN = "user_optin", "Opt-in al registrarse"
        IMPORT = "import", "Importado manualmente"

    email = models.EmailField(unique=True, db_index=True)
    name = models.CharField(max_length=120, blank=True)

    source = models.CharField(
        max_length=32,
        choices=Source.choices,
        default=Source.FOOTER,
    )

    confirmed = models.BooleanField(
        default=False,
        help_text="Reservado para double opt-in futuro",
    )

    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Suscriptor"
        verbose_name_plural = "Suscriptores"

    def __str__(self):
        return self.email

    @property
    def is_active(self) -> bool:
        return self.unsubscribed_at is None

    def unsubscribe(self):
        self.unsubscribed_at = timezone.now()
        self.save(update_fields=["unsubscribed_at"])