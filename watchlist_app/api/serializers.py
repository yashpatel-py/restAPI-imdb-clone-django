from wsgiref.validate import validator
from rest_framework import serializers
from watchlist_app.models import Movie

def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short!")
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    # Validate a single field in serializer it self
    name = serializers.CharField(validators = [name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    # To add new data using "POST" request
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    # To Update the data using "PUT" request
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    # Validation for complete objects
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different!")
        else:
            return data

    # Calidation for single objects
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     return value