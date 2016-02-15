from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from transition import views

urlpatterns = [
    url(r'^transition/$', views.TransitionList.as_view()),
    url(r'^transition/(?P<pk>[0-9]+)/$', views.TransitionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)