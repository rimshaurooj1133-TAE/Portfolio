
from django.shortcuts import render

def portfolio_view(request):
    """
    This function handles requests to the homepage
    and renders the main portfolio HTML page.
    """
    # We will look for a template named 'core/index.html'
    return render(request, 'core/index.html', {})
from django.shortcuts import render
from .models import Project # <-- Import the Project model

def portfolio_view(request):
    """
    Fetches all projects from the database and renders the main page.
    """
    # Query the database to get all Project objects
    all_projects = Project.objects.all()

    # Create a context dictionary to pass data to the template
    context = {
        'projects': all_projects
    }

    return render(request, 'core/index.html', context)