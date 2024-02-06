import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title= django_filters.CharFilter(lookup_expr='icontains', label='type title here')
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')
    published_at = django_filters.DateRangeFilter()
    desc= django_filters.CharFilter(lookup_expr='icontains', label='description')

    class Meta:
        model = Job
        fields = ['title', 'desc','job_nature','job_type','category','location']