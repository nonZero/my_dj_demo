from django.db import models


class Execution(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class Run(models.Model):
    class Status(models.IntegerChoices):
        OK = 1
        NOT_OK = 2
        REALLY_BAD = 3

    execution = models.ForeignKey(Execution, on_delete=models.CASCADE,
                                  related_name="runs")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices)

