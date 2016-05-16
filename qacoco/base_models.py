from django.contrib.auth.models import User
from django.db import models

TYPE_CHOICES = (
			(0, 'Not For Adoption'),
			(1, 'For Adoption'),
	)

SCORE_CHOICES = (
	(0,0),
	(1,1),
	(2,2),
	(3,3),
	)

VIDEO_GRADE = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
)

APPROVAL = (
	(0, 'No'),
	(1, 'Yes'),
	)

class QACocoModel(models.Model):
    user_created = models.ForeignKey(User, related_name ="%(app_label)s_%(class)s_created", editable = False, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_modified = models.ForeignKey(User, related_name ="%(app_label)s_%(class)s_related_modified",editable = False, null=True, blank=True)
    time_modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True