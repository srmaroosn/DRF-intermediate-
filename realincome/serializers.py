from xml.parsers.expat import model
from rest_framework import serializers
from realincome.models import EmployeeSalary, Income

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Income
        fields = '__all__'
        
class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSalary
        fields = ['salary_per_months','working_hours','allowance']