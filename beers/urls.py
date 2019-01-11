from django.conf.urls import url, include

from beers.views import beer_list_view, beer_detail_view

urlpatterns = [
    url('list/',beer_list_view, name='beer-list-view'),
    url('detail/(?P<pk>\d+)',beer_detail_view,name='beer-detail-view'),
]