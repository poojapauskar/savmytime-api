from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from sub_category import views

urlpatterns = [
    url(r'^sub_category/$', views.Sub_categoryList.as_view()),
    url(r'^sub_category/(?P<pk>[0-9]+)/$', views.Sub_categoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)