from findlatinnights.events.views import EventListViewAll, EventListViewByCity
from django_distill import distill_path
from django.urls import path


urlpatterns = [
    distill_path('', EventListViewAll.as_view(), name='event_list'),
    path('city/<str:city_name>/', EventListViewByCity.as_view(), name='event_list_city'),
]
