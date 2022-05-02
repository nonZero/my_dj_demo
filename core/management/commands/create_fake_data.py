import random

from django.core.management.base import BaseCommand

from core.models import Execution, Run


class Command(BaseCommand):
    help = "Create fake data"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int, default=10)

    def handle(self, n, *args, **options):
        for i in range(n):
            o = Execution.objects.create()
            for j in range(3):
                o.runs.create(status=random.choice(Run.Status.choices)[0])
