import django_filters
from .models import *

# from pmarket.project.models import Project

class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexaxt')
    keyword = django_filters.filters.CharFilter(field_name='title',lookup_expr='icontains')

    # minPrice = django_filters.filters.NumberFilter(field_name='price'or 0 ,lookup_expr='gte')
    # maxPrice = django_filters.filters.NumberFilter(field_name='price'or 1000000 ,lookup_expr='lte')

    class Meta:
        model = Project
        # fields = ['title' , 'createAt']
        fields = ('title' ,'keyword')# (... minPrice , maxPrice ,'category', 'createAt'...)


        