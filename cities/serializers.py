from rest_framework import serializers
from cities.models import Cities, LANGUAGE_CHOICES, STYLE_CHOICES


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ('id', 'city', 'service_list')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Cities.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.city = validated_data.get('city', instance.city)
        instance.service_list = validated_data.get('service_list', instance.service_list)
        instance.save()
        return instance