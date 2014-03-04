from django.db import models
from django.db.models.signals import pre_delete, post_save

from dashboard.data_log import delete_log, save_log
from dashboard.models import CocoModel, GENDER_CHOICES
from geography.models import District, Village
from partner.models import Partner

class Animator(CocoModel):
    id = models.AutoField(primary_key = True)
    old_coco_id = models.BigIntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    csp_flag = models.NullBooleanField(null=True, blank=True)
    camera_operator_flag = models.NullBooleanField(null=True, blank=True)
    facilitator_flag = models.NullBooleanField(null=True, blank=True)
    phone_no = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=500, blank=True)
    partner = models.ForeignKey(Partner)
    village = models.ForeignKey(Village, null=True, blank=True)
    district = models.ForeignKey(District, null=True, blank=True)
    assigned_villages = models.ManyToManyField(Village, related_name='assigned_villages', through='AnimatorAssignedVillage', null=True, blank=True)
    total_adoptions = models.PositiveIntegerField(default=0, blank=True, editable=False) 
    
    class Meta:
        unique_together = ("name", "gender", "partner", "district")
    
    def get_village(self):
        return None
    
    def get_partner(self):
        return self.partner.id
    
    def __unicode__(self):
        return  u'%s (%s)' % (self.name, self.village)

post_save.connect(save_log, sender=Animator)
pre_delete.connect(delete_log, sender=Animator)

class AnimatorAssignedVillage(CocoModel):
    id = models.AutoField(primary_key = True)
    animator = models.ForeignKey(Animator)
    village = models.ForeignKey(Village)
    start_date = models.DateField(null=True, blank=True)
