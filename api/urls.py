from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^', include('rest_framework.urls')),
    # url(r'^calculate_insurance/$', views.calculation),
    # url(r'^calculate_insurance/(?P<id>[0-9a-f-]+)$', views.calculation),
    url(r'^calculate_insurance/?(?:/(?P<id>[0-9a-f-]+))?$', views.calculation),
])
