from django.core.management.base import CommandError
from django.contrib.auth.management.commands import createsuperuser as BaseCommand


class Command(BaseCommand):
    """
    Override createsuperuser to prevent unauthorized superuser creation.
    This command is disabled for security reasons.
    """
    
    def handle(self, *args, **options):
        raise CommandError(
            'Creating superusers via this command is disabled for security reasons.\n'
            'Please contact the system administrator if you need admin access.'
        )

