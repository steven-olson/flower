from django.db import models


class Timeline(models.Model):
    """
    They "when" of it. When should something be done?
    """
    objects = models.Manager()

    starts_at = models.DateField(
        blank=True,
        null=True
    )

    ends_at = models.DateField(
        blank=False,
        null=True
    )

    description = models.CharField(
        max_length=500,
        default=""
    )

    class Meta:
        db_table = "timeline"
