from django.db import models

from bharathacks.base.models import AuditModel, TimeAuditModel


class MasterEventList(TimeAuditModel):
    name = models.CharField(max_length=255, primary_key=True)

    def __unicode__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'event_master_list'


class EventType(TimeAuditModel):
    master_event = models.ForeignKey(MasterEventList)
    subcategory = models.CharField(max_length=512)

    def __unicode__(self):
        return '{} : {}'.format(self.name, self.subcategory)

    class Meta:
        db_table = 'event_type'


class Event(AuditModel):

    event_type = models.ForeignKey(EventType)
    name = models.CharField(max_length=512)
    location = models.TextField(default='')
    scheduled_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(default='')
    contact_details = models.TextField(default='')
    capacity_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)

    def __unicode__(self):
        return '{} : {}'.format(self.name, self.event_type)

    class Meta:
        db_table = 'events'
