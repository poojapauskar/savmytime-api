from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from category import views

urlpatterns = [
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)