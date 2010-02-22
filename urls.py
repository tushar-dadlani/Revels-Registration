from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    

     (r'^register/$', 'revels2010.register.views.home'),
     (r'^mit/$', 'revels2010.register.views.mit'),
     (r'^$','revels2010.register.views.authentication'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
     (r'^check/','revels2010.register.views.access_check'),
     (r'^outside/$','revels2010.register.views.outsider'),
     (r'^outreg/$','revels2010.register.views.outside'),
#     (r'^next_reg/$','revels2010.register.view.next_reg'),
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
