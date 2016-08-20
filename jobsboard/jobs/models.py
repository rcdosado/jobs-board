from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

from django.db import models


class Job(TimeStampedModel):

    EMPLOYMENT_TYPE_PART_TIME = 1
    EMPLOYMENT_TYPE_FULL_TIME = 2
    EMPLOYMENT_TYPE_FREELANCE = 3
    EMPLOYMENT_TYPE_CONTRACT = 4
    EMPLOYMENT_TYPE_INTERNSHIP = 5

    EMPLOYMENT_TYPE = (
        (EMPLOYMENT_TYPE_PART_TIME, _('Part-time')),
        (EMPLOYMENT_TYPE_FULL_TIME, _('Full-time')),
        (EMPLOYMENT_TYPE_FREELANCE, _('Freelance')),
        (EMPLOYMENT_TYPE_CONTRACT, _('Contract')),
        (EMPLOYMENT_TYPE_INTERNSHIP, _('Internship')),
    )

    creator = models.ForeignKey('auth.User')
    title = models.CharField(max_length=40)
    description = models.TextField()
    url = models.URLField()
    is_featured = models.BooleanField(default=False)
    employment_type = models.IntegerField(choices=EMPLOYMENT_TYPE, default=1)