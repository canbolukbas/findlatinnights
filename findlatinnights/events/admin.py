from django.contrib import admin
from django.utils.html import format_html
from findlatinnights.events.models import Event, Venue, City, Country


def weekday(d):
    # Returns the weekday of the datetime object d
    # Monday is 0 and Sunday is 6
    return d.weekday()

class WeekdayListFilter(admin.SimpleListFilter):
    title = 'weekday'
    parameter_name = 'weekday'

    def lookups(self, request, model_admin):
        # list of tuples. The first element in each tuple is the coded value 
        # for the option that will appear in the URL query. The second element 
        # is the human-readable name for the option that will appear in the 
        # right sidebar.
        return [
            ('2', 'Monday'),
            ('3', 'Tuesday'),
            ('4', 'Wednesday'),
            ('5', 'Thursday'),
            ('6', 'Friday'),
            ('7', 'Saturday'),
            ('1', 'Sunday'),
        ]

    def queryset(self, request, queryset):
        if self.value():
            # Compare the requested value (either '1', '2', '3', '4', '5', '6', '7') 
            # to the weekday field in the date object
            return queryset.filter(start_datetime__week_day=self.value()) 
        else:
            return queryset

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = (WeekdayListFilter, )
    list_display = ('title', 'display_link', )

    def display_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.external_url)
    display_link.short_description = 'External URL'

admin.site.register([Venue, City, Country])
