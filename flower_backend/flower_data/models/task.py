from django.db import models


class Task(models.Model):
    """
    Representation of something to be done. Needs to have an explicit link to a goal
    and a timeline and nothing else.
    """
    objects = models.Manager()

    parent_goal = models.ForeignKey(
        "flower_data.goal",
        on_delete=models.PROTECT,
        default=None,
        blank=True,
        null=True
    )

    timeline = models.ForeignKey(
        "flower_data.timeline",
        on_delete=models.PROTECT,
        default=None,
        blank=True,
        null=True
    )

    description = models.TextField(
        max_length=300,
        blank=False
    )

    class Meta:
        db_table = "task"
