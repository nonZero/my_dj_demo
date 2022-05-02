from rest_framework import serializers

from . import models


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Run
        fields = "__all__"


class ExecutionSerializer(serializers.HyperlinkedModelSerializer):
    runs = RunSerializer(many=True, read_only=True)
    last_run_status = serializers.IntegerField()

    class Meta:
        model = models.Execution
        fields = "__all__"
        # fields = [
        #     "__all__",
        #     "runs",
        # ]
