from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from indicators.models import Indicator
from indicators.serializers import IndicatorSerializer


class ListCreateSymbolsAPIView(ListCreateAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer


class GetUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
