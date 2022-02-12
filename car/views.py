from rest_framework import viewsets
from car.models import CarPlan, CarSpecification
from car.serializers import CarPlanSerializer, CarSpecificationSerializer

# Create your views here.
class CarPlanViewset(viewsets.ModelViewSet):
    queryset = CarPlan.objects.all()
    serializer_class= CarPlanSerializer


class CarSpecificationViewset(viewsets.ModelViewSet):
    queryset = CarSpecification.objects.all()
    serializer_class = CarSpecificationSerializer

    def create(self, request, *args, **kwargs,):
        carplan_id= request.data.get('car_plan')
        carplan = CarPlan.objects.get(id= carplan_id)
        carspecs = CarSpecification.objects.create(
            car_plan= carplan,
            car_brand= request.data.get('car_brand'),
            car_model= request.data.get('car_model'),
            manufacture_year= request.data.get('manufacture_year')
        )
        serializer = CarSpecificationSerializer(carspecs)
        serializer.save()
    