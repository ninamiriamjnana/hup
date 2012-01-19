from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hup.views.home', name='home'),
    # url(r'^hup/', include('hup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^weblog/', include('zinnia.urls')), #zinnia
    url(r'^comments/', include('django.contrib.comments.urls')),#zinnia



)
urlpatterns += staticfiles_urlpatterns()
