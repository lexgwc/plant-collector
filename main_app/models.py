from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

TIMES_OF_DAY = (
    ('M', 'Morning'),
    ('N', 'Noon'),
    ('E', 'Evening')
)

class Tool(models.Model):
   type = models.CharField(max_length=100)
   color = models.CharField(max_length=100)
   def __str__(self):
    return self.name

class Plant(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    origin = models.CharField(max_length=100)
    tools = models.ManyToManyField(Tool)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Watering(models.Model):
  date = models.DateField('Watering Date')
  time_of_day = models.CharField(
    max_length=1,
    choices=TIMES_OF_DAY,
    default=TIMES_OF_DAY[0][0]
    )
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.get_watering_display()} on {self.date}"
  class Meta:
    ordering = ['-date']


  