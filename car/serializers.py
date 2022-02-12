from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import CarPlan, CarSpecification

class CarPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPlan
        fields = '__all__'

class CarSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecification
        fields = ['car_plan','car_brand','car_model','manufacture_year']