from rest_framework import serializers
from .models import Plant, Watering, Tool

class ToolSerializer(serializers.ModelSerializer):
   class Meta:
      model = Tool
      fields = '__all__'
      read_only_fields = ('plant',)
      
class PlantSerializer(serializers.ModelSerializer):
   watered_for_today = serializers.SerializerMethodField()
   tools = ToolSerializer(many=True, read_only=True) 

   class Meta:
    model = Plant
    fields = '__all__'
    
    def get_watered_for_today(self, obj):
       return obj.watered_for_today()


class WateringSerializer(serializers.ModelSerializer):
  class Meta:
    model = Watering
    fields = '__all__'
    read_only_fields = ('plant',)
