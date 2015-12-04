from activities.models import PersonAdoptPractice, PersonMeetingAttendance, Screening
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

#14 - Maharashtra - MSSRF:29
#9 - UP - PANI:19
#4 - Karnataka - IDF:27
#15 - Telangana - SERP:9
#1 - MP - MPRAF:34


state_id = 14
partner_id = 27
limit = 10000

person_list = Person.objects.filter(village__block__district__state_id = state_id).values_list('id',flat=True)
person_list = list(person_list)

video_seen_list = Video.objects.filter(village__block__district__state_id=state_id).values_list('id',flat=True).distinct()
video_seen_list = list(video_seen_list)
print video_seen_list

for i in range(1,limit):

    person = Person.objects.get(id = random.choice(person_list))
    partner = Partner.objects.get(id = partner_id)
    video = Video.objects.get(id = random.choice(video_seen_list))
    start_date = datetime.date.today().replace(day=1, month=1).toordinal()
    end_date = datetime.date.today().toordinal()
    random_day = datetime.date.fromordinal(random.randint(start_date, end_date))
    print random_day

    year = random.choice([2014,2015])
    month = random.choice(range(1, 10))
    day = random.choice(range(1, 28))
    birth_date = datetime.date(year, month, day)

    fix_date = datetime.date(2014, 10, 30)

    try:
        p = PersonAdoptPractice(person = person, partner = partner, date_of_adoption = random_day,video = video)
        print i
        p.save()
    except Exception:
        try:
            video2 = Video.objects.get(id = random.choice(video_seen_list))
            p = PersonAdoptPractice(person = person, partner = partner, date_of_adoption = birth_date,video = video2)
            print i
            p.save()
        except Exception:
            video2 = Video.objects.get(id = random.choice(video_seen_list))
            person = Person.objects.get(id = random.choice(person_list))
            p = PersonAdoptPractice(person = person, partner = partner, date_of_adoption = fix_date,video = video2)
            print i
            p.save()