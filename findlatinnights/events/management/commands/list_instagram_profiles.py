import re

from django.core.management.base import BaseCommand

from findlatinnights.events.models import Event


class Command(BaseCommand):
    help = "Print the external urls of the events in the form of an instagram profile."

    def handle(self, *args, **options):
        regex = re.compile(r'^https://www\.instagram\.com/[^/]+/$')
        url_list = list(Event.objects.values_list('external_url', flat=True).distinct())
        profile_urls = [url for url in url_list if regex.match(url)]
        for p in profile_urls:
            print(p)
