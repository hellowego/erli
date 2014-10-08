from django.conf.urls import patterns, include, url
from erli.views import home
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'erli.views.home', name='home'),
    # url(r'^erli/', include('erli.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^$', home),
    url(r'^$', 'erli.views.home', name='home'),
)


urlpatterns += patterns('',
   (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)