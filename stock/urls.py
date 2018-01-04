from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from scrap import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^", include("scrap.urls")),
##    url(r'^stocks/$', views.StockList.as_view(), name="index"),
    url(r'^json/(?P<rank>\w{0,50})/$', views.json_page, name="json"),
    url(r'^datatable/$', views.datatable, name="datatable"),
    url(r'^table/$', views.table, name="table"),
    url(r'^(?P<rank>\w{0,50})/$', views.chart, name="chart")
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
