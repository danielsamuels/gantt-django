from django.conf.urls import patterns, url

import views, views_json


urlpatterns = patterns(
    '',

    # Standard pages
    url(r'^$', views.Application.as_view(), name='application'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^register/$', views.Registration.as_view(), name='register'),

    # API Pages
    url(r'^data/$', views_json.Data.as_view(), name='data'),
)
