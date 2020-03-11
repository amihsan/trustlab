from rest_framework import serializers
from trustlab.models import Scenario
from trustlab.serializers.stringList_field import StringListField


class ScenarioSerializer(serializers.Serializer):
    name = serializers.CharField()
    agents = StringListField()
    observations = StringListField()
    authority = StringListField()
    instant_feedback = serializers.DictField()
    trust_threshold = serializers.DictField()
    weights = serializers.DictField()
    trust_behavior_1 = serializers.DictField()
    description = serializers.CharField(allow_null=True, allow_blank="True")

    def create(self, validated_data):
        return Scenario(validated_data.get('name'), validated_data.get('agents'), validated_data.get('observations'),
                        validated_data.get('authority'), validated_data.get('instant_feedback'),
                        validated_data.get('trust_threshold'), validated_data.get('weights'),
                        validated_data.get('trust_behavior_1'), validated_data.get('description', ""))

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.agents = validated_data.get('agents', instance.agents)
        instance.observations = validated_data.get('observations', instance.observations)
        instance.authority = validated_data.get('authority', instance.authority)
        instance.instant_feedback = validated_data.get('instant_feedback', instance.instant_feedback)
        instance.trust_threshold = validated_data.get('trust_threshold', instance.trust_threshold)
        instance.weights = validated_data.get('weights', instance.weights)
        instance.trust_behavior_1 = validated_data.get('trust_behavior_1', instance.trust_behavior_1)
        instance.description = validated_data.get('description', instance.description)
        return instance


