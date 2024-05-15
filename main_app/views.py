from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Plant, Watering, Tool
from .serializers import PlantSerializer, WateringSerializer, ToolSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the plant-collector api home route!'}
    return Response(content)



class PlantList(generics.ListCreateAPIView):
  queryset = Plant.objects.all()
  serializer_class = PlantSerializer

class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Plant.objects.all()
  serializer_class = PlantSerializer
  lookup_field = 'id'
  
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    tools_not_associated = Tool.objects.exclude(id__in=instance.tools.all())
    tools_serializer = ToolSerializer(tools_not_associated, many=True)

    return Response({
        'plant': serializer.data,
        'tools_not_associated': tools_serializer.data
    })

class WateringListCreate(generics.ListCreateAPIView):
  serializer_class = WateringSerializer

  def get_queryset(self):
    plant_id = self.kwargs['plant_id']
    return Watering.objects.filter(plant_id=plant_id)

  def perform_create(self, serializer):
    plant_id = self.kwargs['plant_id']
    plant = Plant.objects.get(id=plant_id)
    serializer.save(plant=plant)

class WateringDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = WateringSerializer
  lookup_field = 'id'

  def get_queryset(self):
    plant_id = self.kwargs['plant_id']
    return Watering.objects.filter(plant_id=plant_id)

class ToolList(generics.ListCreateAPIView):
  queryset = Tool.objects.all()
  serializer_class = ToolSerializer
  
class ToolDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Tool.objects.all()
  serializer_class=ToolSerializer
  lookup_field='id'

class AddToolToPlant(APIView):
  def post(self, request, plant_id, tool_id):
    plant = Plant.objects.get(id=plant_id)
    tool = Tool.objects.get(id=tool_id)
    plant.tools.add(tool)
    return Response({'message': f'Tool {tool.name} added to Plant {plant.name}'})