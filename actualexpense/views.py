from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from actualexpense.models import ActaulExpense
#from .permis

from actualexpense.serializers import ActualExpenseSerializer

# Create your views here.
class ExpensesAPIView(ListCreateAPIView):
    queryset = ActaulExpense.objects.all()
    serializer_class = ActualExpenseSerializer
    #permission_classes = (permission.IsAuthenticate)

    def perform_create(self, serializer):
        return serializer.save()(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner =self.request.user)

class ExpenseDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ActaulExpense.objects.all()
    serializer_class = ActualExpenseSerializer
    lookup_field= 'id'
    
    def get_queryset(self):
        return self.queryset.filter(owner =self.request.user)

     
