from rest_framework import serializers
from transition.models import Transition


class TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transition
        fields = ('id', 'transition_id', 'service_id', 'category_id','sub_category_id')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        return Transition.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.service = validated_data.get('service', instance.service)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.sub_category = validated_data.get('sub_category', instance.sub_category)
    #     instance.save()
    #     return instance