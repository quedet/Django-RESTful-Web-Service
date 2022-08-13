from rest_framework import serializers

from api.models import Toy

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'