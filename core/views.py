import django_filters
from django.db.models import OuterRef, Subquery
from django_filters.rest_framework import FilterSet, filters
from rest_framework.viewsets import ModelViewSet

from core.models import Execution, Run
from core.serializers import ExecutionSerializer


class ExecutionFilter(FilterSet):
    last_run_status = filters.ChoiceFilter(
        label="Last Run Status", choices=Run.Status.choices
    )

    class Meta:
        model = Execution
        fields = [
            "last_run_status",
        ]


class ExecutionViewSet(ModelViewSet):
    serializer_class = ExecutionSerializer
    queryset = Execution.objects.all()
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
    ]
    filterset_class = ExecutionFilter

    def get_queryset(self):
        runs = (
            Run.objects.filter(execution=OuterRef("pk"))
            .order_by("-created_at")
            .values("status")
        )
        qs = super().get_queryset().annotate(last_run_status=Subquery(runs[:1]))
        # assert False, qs.query
        return qs
