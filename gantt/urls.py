from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


urlpatterns = patterns(
    '',
    url(r'^', include('gantt.apps.site.urls', namespace='site')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
