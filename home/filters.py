import django_filters
from job.models import Job

class JobFilterr(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='search for job')

    class Meta:
        model = Job
        fields = ['title', 'location','category']