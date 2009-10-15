import settings
from django.conf.urls.defaults import *
from django.contrib import admin
import simplecms.urls
import conferences.urls
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.+)$', 'django.views.static.serve', {'document_root': settings._BASE_DIR + '/../media'}),
    (r'^admin/', include(admin.site.urls)),
)
urlpatterns += conferences.urls.urlpatterns
urlpatterns += simplecms.urls.urlpatterns