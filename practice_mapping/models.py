from django.db import models

from dashboard.models import CocoModel


class Sector(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField()
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class SubSector(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField()
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class Topic(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField()
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class Subtopic(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField()
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class Subject(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField()
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class Practice(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField()
    name = models.CharField(null=True, max_length=200)
    sector = models.ForeignKey(Sector, default=1)
    subsector = models.ForeignKey(SubSector, null=True, blank=True)
    topic = models.ForeignKey(Topic, null=True, blank=True)
    subtopic = models.ForeignKey(Subtopic, null=True, blank=True)
    subject = models.ForeignKey(Subject, null=True, blank=True)

    class Meta:
        verbose_name = "Practice"
        unique_together = ("sector", "subsector", "topic", "subtopic", "subject")

    def __unicode__(self):
        sector = '' if self.sector is None else self.sector.name
        subject = '' if self.subject is None else self.subject.name
        subsector = '' if self.subsector is None else self.subsector.name
        topic = '' if self.topic is None else self.topic.name
        subtopic = '' if self.subtopic is None else self.subtopic.name
        return "%s, %s, %s, %s, %s" % (sector, subject, subsector, topic, subtopic)
