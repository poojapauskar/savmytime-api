from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cities import views

urlpatterns = [
    url(r'^cities/$', views.CitiesList.as_view()),
    url(r'^cities/(?P<pk>[0-9]+)/$', views.CitiesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)