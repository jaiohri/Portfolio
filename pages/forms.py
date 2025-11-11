from django import forms
from .models import Experience

class ExperienceForm(forms.ModelForm):
    """Form for adding/editing experience entries"""
    
    class Meta:
        model = Experience
        fields = ['title', 'company', 'image', 'start_date', 'end_date', 'description', 'display_order']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-300 focus:border-transparent',
                'placeholder': 'e.g., Full Stack Developer'
            }),
            'company': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-300 focus:border-transparent',
                'placeholder': 'e.g., Tech Company Inc'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-yellow-300 file:text-gray-900 hover:file:bg-yellow-200 focus:outline-none focus:ring-2 focus:ring-yellow-300 focus:border-transparent',
                'accept': 'image/*'
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white focus:outline-none focus:ring-2 focus:ring-yellow-300 focus:border-transparent'
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white focus:outline-none focus:ring-2 focus:ring-yellow-300 focus:border-transparent'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-300 focus:border-transparent resize-y min-h-[120px]',
                'rows': 5,
                'placeholder': 'Describe your role and achievements... (Markdown supported: **bold**, *italic*, - lists, etc.)'
            }),
            'display_order': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-white/20 border border-white/30 text-white focus:outline-none focus:ring-2 focus:ring-yellow-300 focus:border-transparent',
                'placeholder': '0',
                'min': '0'
            }),
        }
        labels = {
            'title': 'Job Title',
            'company': 'Company Name',
            'image': 'Company Logo / Image',
            'start_date': 'Start Date',
            'end_date': 'End Date (leave blank if current)',
            'description': 'Description',
            'display_order': 'Display Order (lower numbers appear first)',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make end_date and image not required
        self.fields['end_date'].required = False
        self.fields['display_order'].required = False
        self.fields['image'].required = False

