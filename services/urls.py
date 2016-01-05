from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from services import views

urlpatterns = [
    url(r'^services/$', views.ServicesList.as_view()),
    url(r'^services/(?P<pk>[0-9]+)/$', views.ServicesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)