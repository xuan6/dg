import datetime
from django.db import models
from django.contrib.auth.models import User
from geographies.models import District
from programs.models import Partner

class QaCocoUser(models.Model):
	user = models.ForeignKey(User)
	partner = models.ForeignKey(Partner)
	districts = models.ManyToManyField(District)
	def get_districts(self):
		return self.districts.all()
	
	def __unicode__(self):
		return  u'%s' % (self.user.username)