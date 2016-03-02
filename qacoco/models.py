import datetime
from django.db import models
from django.contrib.auth.models import User

class QaCocoUser(models.Model):
	user = models.ForeignKey(User)
	
	def __unicode__(self):
		return  u'%s' % (self.user.username)