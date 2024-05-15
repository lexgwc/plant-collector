from django.urls import path
from .views import Home, PlantList, PlantDetail, WateringListCreate,WateringDetail, ToolList, ToolDetail, AddToolToPlant

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('plants/', PlantList.as_view(), name='plant-list'),
  path('plants/<int:id>/', PlantDetail.as_view(), name='plant-detail'),
  path('plants/<int:plant_id>/waterings/', WateringListCreate.as_view(),name='watering-list-create'),
  path('plants/<int:plant_id>/waterings/<int:id>/', WateringDetail.as_view(),name='watering-detail'),
  path('tools', ToolList.as_view(), name='tool-list'),
  path('tools/<int:id>/',ToolDetail.as_view(), name='tool-detail'),
  path('plants/<int:plant_id>/add_tool/<int:tool_id>/', AddToolToPlant.as_view(), name='add-tool-to-plant'),
]
