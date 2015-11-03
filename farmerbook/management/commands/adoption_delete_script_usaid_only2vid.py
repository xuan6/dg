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

for element in dict_ids.keys():
    for person in dict_ids[element]:
        PersonAdoptPractice.objects.filter(person__id = person, video__id=element).delete()
    print 'deleted   ' + str(person)