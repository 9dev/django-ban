from datetime import datetime, timezone

from django.core.management.base import BaseCommand

from ban.models import Ban


class Command(BaseCommand):
    help = 'Cleans up inactive bans.'

    def handle(self, *args, **options):
        now = datetime.now(timezone.utc)
        Ban.objects.filter(end_date__lte=now).delete()
        self.stdout.write('Successfully cleaned up inactive bans.')
