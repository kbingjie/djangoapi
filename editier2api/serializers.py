from rest_framework import serializers
from .models import Editier2api
from .models import JobFlow


class Editier2apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editier2api
        fields = ["id", "description", "created"]


class JobFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobFlow
        fields = [
            "id",
            "jobFlowName",
            "intervalTime",
            "jobName",
            "countryCode",
            "created",
        ]

    # def get_object(self,obj):
    #     custom_query = models.JobFlow.objects.filter(id=obj.id)
    #     serializer = JobFlowSerializer
