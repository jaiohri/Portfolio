from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Technology(models.Model):
    """Technology used in projects"""
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Project(models.Model):
    """Portfolio project"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Project screenshot or banner")
    github_url = models.URLField(max_length=500, blank=True, null=True)
    # live_url field removed
    technologies = models.ManyToManyField(Technology, related_name='projects', blank=True)
    featured = models.BooleanField(default=False, help_text="Featured projects appear in the featured section")
    display_order = models.PositiveIntegerField(default=0, help_text="Order for display (lower numbers appear first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        """Return list of technology names for template compatibility"""
        return [tech.name for tech in self.technologies.all()]


class Skill(models.Model):
    """Skill displayed on about page"""
    CATEGORY_CHOICES = [
        ('LANG', 'Languages'),
        ('FRAME', 'Frameworks'),
        ('AIML', 'AI/ML'),
        ('BACK', 'Backend/Databases'),
        ('CLOUD', 'Cloud/DevOps'),
        ('TOOL', 'Developer Tools'),
        ('FUND', 'CS Fundamentals'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='OTHER')
    icon = models.CharField(max_length=10, help_text="Emoji or icon character")
    level = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Skill level from 0 to 100"
    )
    display_order = models.PositiveIntegerField(default=0, help_text="Order for display within category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['category', 'display_order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Experience(models.Model):
    """Work experience entry"""
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    image = models.ImageField(upload_to='experiences/', blank=True, null=True, help_text="Company logo or experience image")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if current position")
    description = models.TextField()
    display_order = models.PositiveIntegerField(default=0, help_text="Order for display (lower numbers appear first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', '-start_date']
    
    def __str__(self):
        return f"{self.title} at {self.company}"
    
    @property
    def period(self):
        """Format period string for display"""
        if self.end_date:
            return f"{self.start_date.strftime('%B %Y')} - {self.end_date.strftime('%B %Y')}"
        return f"{self.start_date.strftime('%B %Y')} - Present"
    
    @property
    def is_current(self):
        """Check if this is a current position"""
        return self.end_date is None


class ContactMessage(models.Model):
    """Contact form submission"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    read = models.BooleanField(default=False, help_text="Mark as read after reviewing")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
    def mark_as_read(self):
        """Mark message as read"""
        self.read = True
        self.save(update_fields=['read'])
