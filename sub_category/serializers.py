from rest_framework import serializers
from sub_category.models import Sub_category, LANGUAGE_CHOICES, STYLE_CHOICES


class Sub_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_category
        fields = ('id', 'sub_category', 'category_id')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Sub_category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.sub_category = validated_data.get('sub_category', instance.sub_category)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance