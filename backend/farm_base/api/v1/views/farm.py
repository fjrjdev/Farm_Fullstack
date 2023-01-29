from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from farm_base.api.v1.serializers import (
    FarmListSerializer,
    FarmCreateSerializer,
    FarmDetailSerializer,
)
from farm_base.models import Farm, Owner
from farm_base.api.v1.filters import FarmFilter
from django_filters import rest_framework as filters

from rest_framework.views import Request, Response, status


class FarmListCreateView(generics.ListCreateAPIView):
    queryset = Farm.objects.filter(is_active=True)
    serializer_class = FarmListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FarmFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_name = self.request.query_params.get("owner_name", None)
        document = self.request.query_params.get("document", None)
        if owner_name or document:
            owner = Owner.objects.filter(name=owner_name) | Owner.objects.filter(
                document=document
            )
            farm = Farm.objects.filter(owner__in=owner)
            self.filter = self.filterset_class(self.request.GET, queryset=farm)
            return self.filter.qs

    def get_serializer_class(self):
        if self.request.method == "GET":
            return FarmListSerializer
        else:
            return FarmCreateSerializer

    def perform_create(self, serializer):
        farm = serializer.save()
        area = float(farm.geometry.area)
        centroid = farm.geometry.centroid
        serializer.save(area=area, centroid=centroid)


class FarmRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farm.objects.filter(is_active=True)
    serializer_class = FarmDetailSerializer
