from django.views.generic import ListView
from django.utils import timezone
from findlatinnights.events.models import Event, City
from django.shortcuts import get_object_or_404


class EventListViewAll(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
    ordering = 'start_datetime'

    def get_queryset(self):
        queryset =  super().get_queryset()
        now = timezone.now()
        return queryset.filter(end_datetime__gte=now)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cities = City.objects.all()
        context['all_cities'] = cities
        return context

class EventListViewByCity(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
    ordering = 'start_datetime'

    def get_queryset(self):
        queryset =  super().get_queryset()
        now = timezone.now()
        return queryset.filter(end_datetime__gte=now)

    def get_city(self):
        city_name = self.kwargs.get('city_name')
        return get_object_or_404(City, name__iexact=city_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.get_city()
        context['city'] = city
        context['events'] = context['events'].filter(venue__city=city)
        cities = City.objects.all()
        context['all_cities'] = cities
        return context