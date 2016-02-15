"""savmytime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('services.urls')),
    url(r'^', include('cities.urls')),
    url(r'^', include('category.urls')),
    url(r'^', include('sub_category.urls')),
    url(r'^', include('user_data.urls')),
    url(r'^', include('service_providers.urls')),
    url(r'^', include('upload_image.urls')),
    url(r'^', include('get_details.urls')),
    url(r'^', include('is_admin_login.urls')),
    url(r'^', include('get_services.urls')),
    url(r'^', include('get_sub_category_details.urls')),
    url(r'^', include('transition.urls')),
    url(r'^', include('order.urls')),
]
