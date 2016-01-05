from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from user_data import views

urlpatterns = [
    url(r'^user_data/$', views.User_dataList.as_view()),
    url(r'^user_data/(?P<pk>[0-9]+)/$', views.User_dataDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)