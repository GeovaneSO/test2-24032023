import ipdb
import pandas as pd
from rest_framework import serializers

from .models import Consumer, DiscountRules


class ConsumerSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict):
        if validated_data["consumer_type"] == "Residencial":
            rule = DiscountRules.objects.create(
                tax_type=DiscountRules.RESIDENTIAL,
                min_consumption=0,
                max_consumption=10000,
                discount=0.18,
                coverage=0.9,
            )
        if validated_data["consumer_type"] == "Comercial":
            rule = DiscountRules.objects.create(
                tax_type=DiscountRules.COMMERCIAL,
                min_consumption=10001,
                max_consumption=20000,
                discount=0.22,
                coverage=0.95,
            )
        if validated_data["consumer_type"] == "Industrial":
            rule = DiscountRules.objects.create(
                tax_type=DiscountRules.INDUSTRIAL,
                min_consumption=20001,
                max_consumption=None,
                discount=0.25,
                coverage=0.99,
            )

        return Consumer.objects.create(**validated_data, discount_rule=rule)

    class Meta:
        model = Consumer
        fields = "__all__"


class DiscountRulesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        consumer = Consumer.objects.get(validated_data['name'])

        if validated_data['consumer_type'] == "Residencial":
            role = DiscountRules.objects.create(
            tax_type=DiscountRules.RESIDENTIAL,
            min_consumption=0,
            max_consumption=10000,
            discount=0.18,
            coverage=0.9
            
        )
        if validated_data['consumer_type'] == "Comercial":

            role = DiscountRules.objects.create(
                tax_type=DiscountRules.COMMERCIAL,
                min_consumption=10001,
                max_consumption=20000,
                discount=0.22,
                coverage=0.95
            )
        if validated_data['consumer_type'] == "Industrial":


            role =DiscountRules.objects.create(
                tax_type=DiscountRules.INDUSTRIAL,
                min_consumption=20001,
                max_consumption=None,
                discount=0.25,
                coverage=0.99
            )
        consumer.discount_rule.add(role)

    class Meta:
        model = DiscountRules
        fields = "__all__"
