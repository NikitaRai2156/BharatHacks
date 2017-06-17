from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin, DetailView

from .models import *


class FeedView(SingleObjectMixin, ListView):

    template_name = 'events/feed.html'
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
        # return super(CmsMisView, self).dispatch(*args, **kwargs)

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
        # return super(CmsObjectDetailView, self).dispatch(*args, **kwargs)


