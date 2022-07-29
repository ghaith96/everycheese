from ctypes import util
from enum import auto
from django.db import models
from autoslug import AutoSlugField

import model_utils.models

class Cheese(model_utils.models.TimeStampedModel):
    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-soft"
        SEMI_HARD = "semi-hard", "Semi-hard"
        HARD = "hard", "Hard"

    name = models.CharField("Name of cheese", max_length=255)
    slug = AutoSlugField("Cheese address", unique=True, always_update=False, populate_from='name')
    description = models.TextField("Description", blank=True)
    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)

    def __str__(self) -> str:
        return self.name
