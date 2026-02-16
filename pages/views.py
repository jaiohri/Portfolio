from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Project, Skill, Experience, ContactMessage
from .forms import ExperienceForm

def is_admin(user):
    """Check if user is admin (not guest)"""
    return user.is_authenticated and user.username != 'guest' and (user.is_staff or user.is_superuser)

def home(request):
    """Home page view"""
    context = {
        'title': 'Welcome to My Personal Website',
        'name': 'Jai Ohri',
        'tagline': 'Developer, Designer, and Problem Solver',
        'about': 'I am passionate about creating innovative solutions and building meaningful digital experiences.',
    }
    return render(request, 'pages/home.html', context)

def about(request):
    """About page view"""
    # Get skills and experience from database
    skills = Skill.objects.all()
    
    # Group skills by category
    skills_by_category = {}
    for choice_code, choice_name in Skill.CATEGORY_CHOICES:
        category_skills = skills.filter(category=choice_code)
        if category_skills.exists():
            skills_by_category[choice_name] = category_skills
            
    experience = Experience.objects.all()
    
    context = {
        'title': 'About Me',
        'name': 'Jai Ohri',
        'tagline': 'Developer, Designer, and Problem Solver',
        'about': 'I am passionate about creating innovative solutions and building meaningful digital experiences.',
        'skills': skills, # Keep for backward compatibility if needed
        'skills_by_category': skills_by_category,
        'experience': experience,
    }
    
    # Check if request is HTMX
    if request.headers.get('HX-Request'):
        return render(request, 'pages/about_content.html', context)
    
    return render(request, 'pages/about.html', context)

def portfolio(request):
    """Portfolio page view"""
    # Get projects from database
    projects = Project.objects.all()
    featured_project = Project.objects.filter(featured=True).first()
    
    context = {
        'title': 'My Portfolio',
        'name': 'Jai Ohri',
        'projects': projects,
        'featured_project': featured_project,
    }
    
    # Check if request is HTMX
    if request.headers.get('HX-Request'):
        return render(request, 'pages/portfolio_content.html', context)
    
    return render(request, 'pages/portfolio.html', context)

def contact(request):
    """Contact page view"""
    context = {
        'title': 'Get In Touch',
        'name': 'Jai Ohri',
        'contact_info': {
            'email': 'jai@example.com',
            'phone': '+1 (555) 123-4567',
            'location': 'San Francisco, CA',
            'linkedin': 'https://linkedin.com/in/jai-ohri',
            'github': 'https://github.com/jai-ohri',
            'twitter': 'https://twitter.com/jai_ohri'
        }
    }
    
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
        
        if request.headers.get('HX-Request'):
            return render(request, 'pages/contact_success.html', {
                'message': f'Thank you {name}! Your message has been sent successfully.'
            })
        else:
            messages.success(request, f'Thank you {name}! Your message has been sent successfully.')
    
    # Check if request is HTMX
    if request.headers.get('HX-Request'):
        return render(request, 'pages/contact_content.html', context)
    
    return render(request, 'pages/contact.html', context)

def add_experience(request):
    """Add a new experience entry - Admin only"""
    # Check if user is admin, redirect to login if not
    if not is_admin(request.user):
        messages.warning(request, 'You must be logged in as admin to add experiences.')
        return redirect('pages:login')
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            experience = form.save()
            messages.success(request, f'Experience "{experience.title} at {experience.company}" added successfully!')
            return redirect('pages:experiences')
    else:
        form = ExperienceForm()
    
    context = {
        'title': 'Add Experience',
        'name': 'Jai Ohri',
        'form': form,
    }
    return render(request, 'pages/add_experience.html', context)

def experiences(request):
    """List all experience entries - Admin only"""
    # Check if user is admin, redirect to login if not
    if not is_admin(request.user):
        messages.warning(request, 'You must be logged in as admin to edit experiences.')
        return redirect('pages:login')
    
    experiences_list = Experience.objects.all()
    
    context = {
        'title': 'Edit Experiences',
        'name': 'Jai Ohri',
        'experiences': experiences_list,
        'is_admin': is_admin(request.user),
    }
    return render(request, 'pages/experiences.html', context)

def edit_experience(request, experience_id):
    """Edit an existing experience entry - Admin only"""
    # Check if user is admin, redirect to login if not
    if not is_admin(request.user):
        messages.warning(request, 'You must be logged in as admin to edit experiences.')
        return redirect('pages:login')
    
    try:
        experience = Experience.objects.get(id=experience_id)
    except Experience.DoesNotExist:
        messages.error(request, 'Experience not found.')
        return redirect('pages:experiences')
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES, instance=experience)
        if form.is_valid():
            experience = form.save()
            messages.success(request, f'Experience "{experience.title} at {experience.company}" updated successfully!')
            return redirect('pages:experiences')
    else:
        form = ExperienceForm(instance=experience)
    
    context = {
        'title': 'Edit Experience',
        'name': 'Jai Ohri',
        'form': form,
        'experience': experience,
    }
    return render(request, 'pages/edit_experience.html', context)

def delete_experience(request, experience_id):
    """Delete an experience entry - Admin only"""
    # Check if user is admin, redirect to login if not
    if not is_admin(request.user):
        messages.warning(request, 'You must be logged in as admin to delete experiences.')
        return redirect('pages:login')
    
    try:
        experience = Experience.objects.get(id=experience_id)
        experience_title = f"{experience.title} at {experience.company}"
        experience.delete()
        messages.success(request, f'Experience "{experience_title}" deleted successfully!')
    except Experience.DoesNotExist:
        messages.error(request, 'Experience not found.')
    
    return redirect('pages:experiences')

def login_view(request):
    """Admin login page"""
    if request.user.is_authenticated and is_admin(request.user):
        return redirect('pages:home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            next_url = request.GET.get('next', None)
            if next_url:
                return redirect(next_url)
            return redirect('pages:home')
    else:
        form = AuthenticationForm()
    
    context = {
        'title': 'Admin Login',
        'name': 'Jai Ohri',
        'form': form,
    }
    return render(request, 'pages/login.html', context)

@login_required
def logout_view(request):
    """Logout and redirect to home"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('pages:home')

def favicon(request):
    """Handle favicon requests - return 204 No Content"""
    return HttpResponse(status=204)
