from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    """Defines the structure for a portfolio project entry."""
    title = models.CharField(max_length=150)
    description = models.TextField()
    tech_stack = models.CharField(
        max_length=250,
        help_text="List the primary technologies (e.g., Django, DRF, PostgreSQL)"
    )
    github_url = models.URLField(max_length=300, blank=True, null=True)
    live_demo_url = models.URLField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Sort projects by most recently created/added by default
        ordering = ['-created_at']
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title