from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#djangobb?
from sitemap import SitemapForum, SitemapTopic
from forms import RegistrationFormUtfUsername
from djangobb_forum import settings as forum_settings

#djangobb?
sitemaps = {
    'forum': SitemapForum,
    'topic': SitemapTopic,
}


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hup.views.home', name='home'),
    # url(r'^hup/', include('hup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^news/', include('zinnia.urls')), #zinnia
    url(r'^comments/', include('django.contrib.comments.urls')),#zinnia

    (r'^forum/', include('djangobb_forum.urls', namespace='djangobb')), #djangobb
   



)
urlpatterns += staticfiles_urlpatterns()





# PM Extension
if (forum_settings.PM_SUPPORT):
    urlpatterns += patterns('',
        (r'^forum/pm/', include('messages.urls')),
   )



