from rest_framework import serializers

from api.models import Toy

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.toy_category = validated_data.get('toy_category', instance.toy_category)
    #     instance.was_included_in_home = validated_data.get('was_included_in_home', instance.was_included_in_home)
    #     instance.release_date = validated_data.get('release_date', instance.release_date)
    #     instance.save()
    #     return instance