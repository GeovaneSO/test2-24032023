from rest_framework import serializers
from .models import Consumer
import pandas as pd


class ConsumerSerializer(serializers.ModelSerializer):

    def create(self, validated_data: dict):
        ...

    class Meta:
        model = Consumer
        fields = '__all__'