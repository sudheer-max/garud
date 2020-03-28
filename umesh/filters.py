import django_filters
from .models import *

class DomesticFilter(django_filters.FilterSet):
    class Meta: 
        model = Domestic
        fields = ['tag', 'inclusiones',]
