from rest_framework import serializers
from services.models import Services


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'service', 'image','icon', 'description','created')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Services.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.service = validated_data.get('service', instance.service)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance