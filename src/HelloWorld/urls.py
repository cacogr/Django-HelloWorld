from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from print_string.models import HelloWorld
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',  ListView.as_view(
        model=HelloWorld, template_name='index.html'
    ), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
