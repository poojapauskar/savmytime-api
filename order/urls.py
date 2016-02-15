from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from order import views

urlpatterns = [
    url(r'^order/$', views.OrderList.as_view()),
    url(r'^order/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)