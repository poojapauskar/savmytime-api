from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from service_providers import views

urlpatterns = [
    url(r'^service_providers/$', views.Service_providersList.as_view()),
    url(r'^service_providers/(?P<pk>[0-9]+)/$', views.Service_providersDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)