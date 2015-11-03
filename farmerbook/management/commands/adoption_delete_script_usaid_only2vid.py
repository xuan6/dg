from activities.models import PersonAdoptPractice, PersonMeetingAttendance
from videos.models import Video
from people.models import Person
from programs.models import Partner
import os.path
import csv
import dg.settings
import math
import random
import MySQLdb

import datetime
dict_ids = {3022:[75619, 67200, 86662, 72488, 72560, 72495], 2969:[67200, 86698, 86662, 65530, 72488, 72560]}

adoption_id = PersonAdoptPractice.objects.filter(video__id__in=[3022,2969]).values_list('id',flat=True)
adoption_id = list(adoption_id)
i=0
for element in adoption_id:
    if(i<800):
        PersonAdoptPractice.objects.filter(id=element).delete()
        print 'deleted   ' + str(element)
        i=i+1
    else:
        print "done"
        break