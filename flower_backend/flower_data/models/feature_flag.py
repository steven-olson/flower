from django.db import models
from flower_data.managers.feature_flag_manager import FeatureFlagManager


class FeatureFlag(models.Model):

    objects = FeatureFlagManager

    flag_name = models.CharField(
        max_length=100,
        blank=False
    )

    is_active = models.BooleanField(
        default=False,
        blank=True
    )
