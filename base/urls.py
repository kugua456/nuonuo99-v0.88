from django.conf.urls import patterns, include, url
from django.conf import settings
import xadmin

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns('',
    url(r'^$', 'base.views.home', name='home'),
    url(r'^admin/', include(xadmin.site.urls)),
    url(r'^accounts/', include('userena.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,
             }
            ),
        url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT,
             }
            ),
    )
