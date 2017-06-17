from django.db import models

from bharathacks.base.models import AuditModel, TimeAuditModel


class EventType(TimeAuditModel):
    name = models.CharField(max_length=512)
    subcategory = models.CharField(max_length=512)

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

    class Meta:
        db_table = 'events'
