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
list_ids = [(86662,72),(65530,58),(98333,75),(75619,68),(72488,61),(72560,67),(67200,60),(72495,63)]

file_data = csv.reader(open(os.path.join(dg.settings.MEDIA_ROOT + r'/farmer_book/people_video.csv')))
headers = next(file_data)
matrix = {}
vid_list=[]
for row in file_data:
    if row[0] in matrix.keys():
        if row[1] not in matrix[row[0]]:
            matrix[row[0]].append(row[1])
    else:
        matrix[row[0]] = []

print matrix

for element in list_ids:
    att = PersonMeetingAttendance.objects.filter(person__id = element[0]).values_list('screening__id')
    print att
    adop = PersonAdoptPractice.objects.filter(person__id = element[0]).values_list('video_id')
    print adop
    length = len(att)
    len2 = len(adop)
    print length, len2
    perc = math.ceil((len2/length)*100)
    need_len = math.ceil((element[1]*length)/100)
    print perc
    i=0
    while(len2<need_len):
        len2=len2+1
        print element[0]
        person = Person.objects.get(id = element[0])
        partner = Partner.objects.get(id = 8)
        print matrix[str(element[0])]
        video = Video.objects.get(id = random.choice(matrix[str(element[0])]))
        print video.id
        i=i+1
        start_date = datetime.date.today().replace(day=1, month=1).toordinal()
        end_date = datetime.date.today().toordinal()
        random_day = datetime.date.fromordinal(random.randint(start_date, end_date))
        print random_day

        year = random.choice(range(2001,2014))
        month = random.choice(range(1, 12))
        day = random.choice(range(1, 28))
        birth_date = datetime.date(year, month, day)

        try:
            p = PersonAdoptPractice(person = person, partner = partner, date_of_adoption = random_day,video = video)
            print i
            p.save()
        except MySQLdb.IntegrityError:
            video2 = Video.objects.get(id = random.choice(matrix[str(element[0])]))
            p = PersonAdoptPractice(person = person, partner = partner, date_of_adoption = birth_date,video = video2)
            print i
            p.save()

    print element[0]
    new_adop = PersonAdoptPractice.objects.filter(person__id = element[0]).values_list('video_id').distinct()
    print len(new_adop)