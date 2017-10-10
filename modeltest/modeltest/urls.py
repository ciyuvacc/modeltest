from django.conf.urls import include, url
from django.contrib import admin
from modelphone import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',views.index),
    url(r'^detail/(\d+)$',views.detail,name='detail-url'),
]
