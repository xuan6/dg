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

video_list = [2969,3022, 2972,3032, 3033, 3049, 3068, 3069, 3081, 3090]

person_list = [75619, 67200, 86662, 72488, 72560, 72495,86698,65530,98333]
start_date = datetime.date(2014, 1, 1)
end_date = datetime.date(2015, 10, 31)


adoption_id_all = PersonAdoptPractice.objects.filter(person__village__block__district__id=15,date_of_adoption__range=(start_date,end_date) ).values_list('id',flat=True)
adoption_id_all = list(adoption_id_all)

adoption_id_not = PersonAdoptPractice.objects.filter(person__id__in=person_list, video__id__in=video_list, date_of_adoption__range=(start_date,end_date)).values_list('id',flat=True)
adoption_id_not = list(adoption_id_not)

to_delete = set(adoption_id_all) - set(adoption_id_not)

to_delete = list(to_delete)

print len(to_delete)
i=0
for element in to_delete:
    if(i<2000):
        PersonAdoptPractice.objects.filter(id=element).delete()
        print 'deleted   ' + str(element)
        i=i+1
        print i
    else:
        print "done"
        break