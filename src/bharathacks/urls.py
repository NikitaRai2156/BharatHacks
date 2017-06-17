from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from Profile.views import (
		login_view, 
		register_view, 
		logout_view
		)

from bharathacks.events.views import EventListView

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^events/', EventListView, name='events'),
    



]



