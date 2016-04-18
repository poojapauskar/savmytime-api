from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from edit_cities import views
from edit_cities.views import get_queryset


urlpatterns = [
    url(r'^edit_cities/update/$', views.edit_cityList.as_view()),
    url(r'^edit_cities/$', get_queryset),
    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]