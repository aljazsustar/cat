from rest_framework import serializers

from api.indicators.models import Indicator


class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        fields = '__all__'
