from django.conf.urls import url

from . import views

app_name = 'flea_market'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<ad_id>[0-9]+)/$', views.detail, name='detail'),
]
