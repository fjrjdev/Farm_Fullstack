from farm_base.models import Farm, Owner
from django_filters import rest_framework as filters
from farm_base.api.v1.filters.fields import NumberInFilter


class FarmFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    municipality = filters.CharFilter(
        field_name="municipality", lookup_expr="icontains"
    )
    state = filters.CharFilter(field_name="state", lookup_expr="icontains")

    class Meta:
        model = Farm
        fields = ["owner", "state", "id", "name", "municipality"]
