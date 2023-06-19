from rest_framework import serializers
from flower_data.models import Goal


class GoalDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = "__all__"
