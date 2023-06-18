from django.db import models


class Goal(models.Model):
    """
    They "why" of it, and then some. Why are we doing something?
    What specific business goal is this task achieving?

    This should cleanly map to some more abstract deliverable.
    """
    objects = models.Manager()

    description = models.CharField(
        max_length=300,
        blank=False,
        null=True
    )

    class Meta:
        db_table = "goal"
