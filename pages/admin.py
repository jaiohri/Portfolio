from django.contrib import admin
from .models import Project, Technology, Skill, Experience, ContactMessage


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'display_order', 'created_at']
    list_filter = ['featured', 'created_at', 'technologies']
    search_fields = ['title', 'description']
    filter_horizontal = ['technologies']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Technologies & Display', {
            'fields': ('technologies', 'featured', 'display_order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'level', 'display_order', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    list_editable = ['display_order', 'level']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'is_current', 'display_order']
    list_filter = ['start_date', 'end_date', 'created_at']
    search_fields = ['title', 'company', 'description']
    list_editable = ['display_order']
    fieldsets = (
        ('Position Details', {
            'fields': ('title', 'company', 'image', 'description')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date')
        }),
        ('Display', {
            'fields': ('display_order',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'read', 'created_at']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    list_editable = ['read']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('read',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        """Disable adding messages through admin (only via contact form)"""
        return False
