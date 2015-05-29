"""web_ui URL Configuration

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
from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from web_ui import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='web_ui:list_report')),
    url(r'^reports/$', views.ReportListView.as_view(), name='list_report'),
    url(r'^reports/author/(?P<author_id>[^/]+)/$', views.ReportListView.as_view(), name='list_author_report'),
    url(r'^reports/search/$', views.ReportSearchView.as_view(), name='search_report'),
    url(r'^reports/new/$', views.ReportCreateView.as_view(), name='create_report'),
    url(r'^reports/(?P<pk>\d+)/$', views.ReportDetailView.as_view(), name='show_report'),
    url(r'^reports/(?P<pk>\d+)/edit/$', views.ReportUpdateView.as_view(), name='edit_report'),
    url(r'^reports/(?P<pk>\d+)/delete/$', views.ReportDeleteView.as_view(), name='delete_report'),
]
