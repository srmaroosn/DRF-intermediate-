from rest_framework import serializers

from actualexpense.models import ActaulExpense

class ActualExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActaulExpense
        fields='__all__'