from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project

# Register the Project model here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Customize the list view in the admin panel
    list_display = ('title', 'tech_stack', 'github_url', 'created_at')
    search_fields = ('title', 'tech_stack')