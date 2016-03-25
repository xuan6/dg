import datetime
from django.db import models
from django.contrib.auth.models import User
from geographies.models import Village
from programs.models import Partner

class QaCocoUser(models.Model):
	user = models.ForeignKey(User)
	partner = models.ForeignKey(Partner)
	village = models.ForeignKey(Village)

	def get_villages(self):
		return self.villages.all()

	def __unicode__(self):
		return  u'%s' % (self.user.username)