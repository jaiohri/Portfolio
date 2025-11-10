from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin

class AutoGuestLoginMiddleware(MiddlewareMixin):
    """
    Automatically logs in users as 'guest' if they're not authenticated.
    Guest user is created automatically if it doesn't exist.
    """
    def process_request(self, request):
        # Skip if user is already authenticated
        if request.user.is_authenticated:
            return None
        
        # Skip for login/logout URLs to avoid redirect loops
        if request.path.startswith('/login/') or request.path.startswith('/logout/'):
            return None
        
        # Get or create guest user
        guest_user, created = User.objects.get_or_create(
            username='guest',
            defaults={
                'email': 'guest@example.com',
                'is_staff': False,
                'is_superuser': False,
            }
        )
        
        # Set a password for guest (won't be used since we auto-login)
        if created:
            guest_user.set_unusable_password()
            guest_user.save()
        
        # Auto-login as guest
        if not request.user.is_authenticated:
            login(request, guest_user, backend='django.contrib.auth.backends.ModelBackend')
        
        return None

