from django.conf.urls import include, url

from .views import *

urlpatterns = [

    url(r'^feed/types', (DistincEventView.as_view()), name='event_types'),
    url(r'^detail/(?P<pk>[-\w]+)/$', (EventDetailView.as_view()), name='event_detail'),
    url(r'^feed/', (FeedView.as_view()), name='feed_view'),

]