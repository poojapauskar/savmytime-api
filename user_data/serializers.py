from rest_framework import serializers
from user_data.models import User_data, LANGUAGE_CHOICES, STYLE_CHOICES


class User_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_data
        fields = ('id', 'name', 'phone', 'email','city','service','category','sub_category')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User_data.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.city = validated_data.get('city', instance.city)
        instance.service = validated_data.get('service', instance.service)
        instance.category = validated_data.get('category', instance.category)
        instance.sub_category = validated_data.get('sub_category', instance.sub_category)
        instance.save()
        return instance