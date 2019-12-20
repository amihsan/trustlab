from rest_framework import serializers
from trustlab.models import Scenario
from trustlab.serializers.stringList_field import StringListField


class ScenarioSerializer(serializers.Serializer):
    name = serializers.CharField()
    agents = StringListField()
    schedule = StringListField()
    description = serializers.CharField(allow_null=True, allow_blank="True")

    def create(self, validated_data):
        return Scenario(validated_data.get('name'), validated_data.get('agents'), validated_data.get('schedule'),
                        validated_data.get('description', ""))

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.agents = validated_data.get('agents', instance.agents)
        instance.schedule = validated_data.get('schedule', instance.schedule)
        instance.description = validated_data.get('description', instance.description)
        return instance


