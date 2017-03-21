#  Reference: 'Django Tutorial for Beginners - 39 - REST API Serializer JSON', thenewboston, YouTube [Video] https://www.youtube.com/watch?v=V4NjlXiu5WI&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK&index=39 [Accessed: 28/08/16]

from rest_framework import serializers
from .models import Rooms, Modules, Groundtruth, Timemodule, BinaryPredictions, PercentagePredictions, EstimatePredictions

class SerializerRooms(serializers.ModelSerializer): 
    class Meta:
        model = Rooms
        fields = '__all__'

class SerializerModules(serializers.ModelSerializer): 
    class Meta:
        model = Modules
        fields = '__all__'

class SerializerGroundtruth(serializers.ModelSerializer): 
    class Meta:
        model = Groundtruth
        fields = '__all__'

class SerializerTimemodule(serializers.ModelSerializer): 
    class Meta:
        model = Timemodule
        fields = '__all__'

class SerializerBinaryPredictions(serializers.ModelSerializer): 
    class Meta:
        model = BinaryPredictions
        fields = '__all__'

class SerializerPercentagePredictions(serializers.ModelSerializer): 
    class Meta:
        model = PercentagePredictions
        fields = '__all__'

class SerializerEstimatePredictions(serializers.ModelSerializer): 
    class Meta:
        model = EstimatePredictions
        fields = '__all__'

