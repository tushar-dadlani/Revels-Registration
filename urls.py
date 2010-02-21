from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    

     (r'^register/$', 'revels2010.register.views.home'),
     (r'^/registration/$', 'revels2010.register.views.reg_page'),
     (r'^$','revels2010.register.views.authentication'),
     (r'^check/','revels2010.register.views.access_check'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
