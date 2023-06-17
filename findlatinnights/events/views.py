from django.views.generic import ListView
from findlatinnights.events.models import Event


class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
