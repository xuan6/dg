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

odisha_ppl = Person.objects.filter(village__block__district__state_id = 3).values_list('id',flat=True)
odisha_ppl = set(list(odisha_ppl))
list_ids = [86662,86698,65530,98333,75619,72488,72560,67200,72495]
odisha_ppl = odisha_ppl - set(list_ids)
print type(odisha_ppl)
odisha_ppl = list(odisha_ppl)
print type(odisha_ppl)
start_date = datetime.date(2014, 1, 1)
end_date = datetime.date(2015, 10, 31)
adoption_ids = PersonAdoptPractice.objects.filter(person__id__in=odisha_ppl, date_of_adoption__range=(start_date,end_date)).values_list('id', flat=True)
adoption_ids = list(adoption_ids)
print adoption_ids
print random.choice(adoption_ids)
for i in range(1,15000):
    adop_id = random.choice(adoption_ids)
    adoption_ids.remove(adop_id)
    PersonAdoptPractice.objects.filter(id=adop_id).delete()
    print str(i) + '   ' + str(adop_id) + '   deleted'