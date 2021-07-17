import django_filters

from .models import transactions

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = transactions
        fields = ['Month','Year']

class OrderFilter1(django_filters.FilterSet):
    class Meta:
        model = transactions
        fields = ['Year']

class OrderFilter2(django_filters.FilterSet):
    class Meta:
        model = transactions
        fields = ['Month','Year','user']

class OrderFilter3(django_filters.FilterSet):
    class Meta:
        model = transactions
        fields = ['user']