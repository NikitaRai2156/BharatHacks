from django.contrib import admin

from .models import *

@admin.register(MasterEventList)
class MasterEventListAdmin(admin.ModelAdmin):
    pass


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
