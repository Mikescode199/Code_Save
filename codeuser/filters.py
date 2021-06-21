import django_filters
from .models import * 

class SnippeFilter(django_filters.FilterSet):

    class Meta:
        model = Snippet
        fields = ['lenguajeProgramacion', 'categoria']