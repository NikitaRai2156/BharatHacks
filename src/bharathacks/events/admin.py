from django.contrib import admin

from .models import MasterEventList,EventType,Event

# @admin.register(MasterEventList)
# class MasterEventListAdmin(admin.ModelAdmin):
#     pass


# @admin.register(EventType)
# class EventTypeAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     pass



admin.site.register(MasterEventList)
admin.site.register(EventType)
admin.site.register(Event)