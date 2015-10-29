from activities.models import PersonAdoptPractice, PersonMeetingAttendance
list_ids = [(67200,69),(86698,64),(86662,72),(65530,58),(98333,75),(75619,68),(72488,61),(72560,67),(72495,63)]
for tup in list_ids:
	att = PersonMeetingAttendance.objects.filter(person__id = tup[0])
	length = len(att)
	print length