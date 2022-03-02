from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from realincome.models import EmployeeSalary, Income
from realincome.serializers import EmployeeSalarySerializer, IncomeSerializer
from rest_framework import permissions
from realincome .permissions import IsOwner
from rest_framework import viewsets
# Create your views here.
class IncomeListAPIView(ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class= IncomeSerializer
    #permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user.id)

    def get_queryset(self):
        return self.queryset.filter(owner = self.request.user.id)

class IncomeDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class=  IncomeSerializer
    lookup_field = 'id'
    #permission_classes = (permissions.IsAuthenticated,IsOwner, )


    def get_queryset(self):
        return self.queryset.filter(owner = self.request.user)

class EmployeeSalaryViewViewset(viewsets.ModelViewSet):
    serializer_class =   EmployeeSalarySerializer
    querysets =  EmployeeSalary.objects.all()