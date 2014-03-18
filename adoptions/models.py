from django.db import models
from django.db.models.signals import pre_delete, post_save

from dashboard.data_log import delete_log, save_log
from dashboard.models import CocoModel
from partner.models import Partner
from people.models import Person
from video.models import Video


class PersonAdoptPractice(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField()
    person = models.ForeignKey(Person)
    video = models.ForeignKey(Video)
    prior_adoption_flag = models.NullBooleanField(null=True, blank=True)
    date_of_adoption = models.DateField()
    quality = models.CharField(max_length=200, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    quantity_unit = models.CharField(max_length=150, blank=True)
    time_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    partner = models.ForeignKey(Partner)

    def __unicode__(self):
        return "%s (%s) (%s) (%s)" % (self.person.person_name, self.person.father_name, self.person.village.village_name, self.video.title)

    def get_village(self):
        return self.person.village.id

    def get_partner(self):
        return self.partner.id

    class Meta:
        unique_together = ("person", "video", "date_of_adoption")
post_save.connect(save_log, sender=PersonAdoptPractice)
pre_delete.connect(delete_log, sender=PersonAdoptPractice)
