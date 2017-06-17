from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin, DetailView

from .models import *


class DistincEventView(SingleObjectMixin, ListView):

    template_name = 'events/feed_home.html'
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
        # return super(FeedView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        event_master_list = MasterEventList.objects.all()
        print event_master_list
        return render(request, self.template_name, {
            'event_types': event_master_list
        })

class FeedView(SingleObjectMixin, ListView):

    template_name = 'events/feed.html'
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
        # return super(FeedView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        return render(request, self.template_name, {
            'events': events
        })

class EventDetailView(DetailView):

    template_name = 'events/detail.html'
    model = Event
    context_object_name = 'event'

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
        # return super(EventDetailView, self).dispatch(*args, **kwargs)


