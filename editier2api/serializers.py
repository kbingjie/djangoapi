from rest_framework import serializers
from .models import Editier2api


class Editier2apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editier2api
        fields = ["id", "description", "created"]
