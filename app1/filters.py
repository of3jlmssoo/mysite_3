# from django.contrib.auth.models import Usercr
import django_filters
from django.conf import settings
from .models import Person

class UserFilter(django_filters.FilterSet):
    # year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    class Meta:
        model = Person
        # fields = ['name', 'yourmultichoice2', 'person_browser']
        fields = {
                'sw_name':['contains'], 
                # 'yourmultichoice2':['exact'],
                # 'person_browser':['contains'],
                # 'person_initial_date': ['year', 'year__gt', 'year__lt', ],
                'sw_mnt_update_date': [ 'range', ],
        }
    
    def get(self, request, *args, **kwargs):
        print("===========================>")