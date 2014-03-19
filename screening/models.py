from django.db import models
from django.db.models.signals import pre_delete, post_save

from dashboard.data_log import delete_log, save_log
from dashboard.models import CocoModel
from geography.models import Village
from partner.models import Partner
from people.models import Animator, Person, PersonGroup
from video.models import Video


class Screening(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200, blank=True)
    target_person_attendance = models.IntegerField(null=True, blank=True)
    target_audience_interest = models.IntegerField(null=True, blank=True)
    target_adoptions = models.IntegerField(null=True, blank=True)
    village = models.ForeignKey(Village)
    animator = models.ForeignKey(Animator)
    farmer_groups_targeted = models.ManyToManyField(PersonGroup)
    videoes_screened = models.ManyToManyField(Video)
    farmers_attendance = models.ManyToManyField(Person, through='PersonMeetingAttendance', blank='False', null='False')
    partner = models.ForeignKey(Partner)

    class Meta:
        unique_together = ("date", "start_time", "end_time","animator","village")

    def __unicode__(self):
        return u'%s %s' % (self.date, self.village)

#pre_save.connect(Person.date_of_joining_handler, sender=Screening)
#m2m_changed.connect(Video.update_viewer_count, sender=Screening.videoes_screened.through)
post_save.connect(save_log, sender=Screening)
pre_delete.connect(delete_log, sender=Screening)


class PersonMeetingAttendance(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField()
    screening = models.ForeignKey(Screening)
    person = models.ForeignKey(Person)
    interested = models.BooleanField(db_index=True)
    expressed_question = models.CharField(max_length=500, blank=True)
    expressed_adoption_video = models.ForeignKey(Video, related_name='expressed_adoption_video', null=True, blank=True)

    def __unicode__(self):
        return  u'%s' % (self.id)
#post_delete.connect(Person.date_of_joining_handler, sender = PersonMeetingAttendance)
#pre_delete.connect(Video.update_viewer_count, sender = PersonMeetingAttendance)
#pre_save.connect(Person.date_of_joining_handler, sender = PersonMeetingAttendance)
#pre_save.connect(Video.update_viewer_count, sender = PersonMeetingAttendance)
