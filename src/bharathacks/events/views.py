from django.shortcuts import render

from .models import MasterEventList,EventType,Event

def EventListView(request):
    event_list = Event.objects.all()
    context = {
        "objects" : event_list,
    }

    return render(request,"events.html",context)


