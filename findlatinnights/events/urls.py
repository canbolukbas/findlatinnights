from findlatinnights.events.views import EventListView
from django_distill import distill_path


urlpatterns = [
    distill_path('', EventListView.as_view(), name='event_list'),
]
