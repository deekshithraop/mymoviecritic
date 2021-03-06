from django.conf.urls import patterns, include, url
from django.contrib import admin
from myapp.api import v1_api
from myapp import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',views.index,name='index'),                   
)
