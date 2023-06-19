from django.views.generic import ListView
from django.utils import timezone
from findlatinnights.events.models import Event


class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
    ordering = 'start_datetime'

    def get_queryset(self):
        queryset =  super().get_queryset()
        now = timezone.now()
        return queryset.filter(end_datetime__gte=now)
