from django.conf.urls import url, include

from beers import views
from beers.views import BeerListView, BeerDetailView, CompanyEditView, CompanyDetailView, CompanyListView

urlpatterns = [
    url(r'^list/$',BeerListView.as_view(), name='beer-list-view'),
    url(r'^detail/(?P<pk>\d+)$',BeerDetailView.as_view(),name='beer-detail-view'),

    url(r'^company/edit/(?P<pk>\d+)$',CompanyEditView.as_view(),name='company-edit-view'),
    url(r'^company/detail/(?P<pk>\d+)$',CompanyDetailView.as_view(),name='company-detail-view'),
    url(r'^company/list/$',CompanyListView.as_view(),name='company-list-view'),
]

handler404 = views.error404