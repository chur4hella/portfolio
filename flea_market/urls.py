from django.conf.urls import url

from . import views

app_name = 'flea_market'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^c(?P<number_cat>[0-9]+)/$', views.products, name='products'),
    # url(r'^upload-ad/$', views.upload_ad, name='upload_ad'),
    url(r'^(?P<ad_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'add/$', views.add_ad, name='add_ad'),
    url(r'^login.*', views.check_login, name='login'),
    url(r'^registration.*', views.registration, name='registration'),
]
