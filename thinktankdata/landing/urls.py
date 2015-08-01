from django.conf.urls import patterns, url
from landing.views import *

urlpatterns = [
    url(r'^$', FrontPageList.as_view(), name='index'),
#    url(r'^season/(?P<slug>[a-zA-Z0-9_-]+).html$', WeekDetail.as_view(), name='week'),
#    url(r'^(?P<slug>[a-zA-Z0-9_-]+).html$', CollectionTemplateView.as_view(), name='collection'),
#    url(r'^$', IndexView.as_view(), name='index'),
]
