"""django_products URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from products.views import PricesDayArchiveView, PricesWeekArchiveView, PricesMonthArchiveView, PricesListJSONView

urlpatterns = [
    url(r'^calendario/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$', PricesDayArchiveView.as_view(), name='calendario_day'),
    url(r'^calendario/(?P<year>[0-9]{4})/week/(?P<week>[0-9]+)/$', PricesWeekArchiveView.as_view(), name="calendario_week"),
    url(r'^calendario/(?P<year>[0-9]{4})/month/(?P<month>[0-9]+)/$', PricesMonthArchiveView.as_view(), name="calendario_month"),
    url(r'^json/(?P<date_start>\d{4}-\d{2}-\d{2})/(?P<date_end>\d{4}-\d{2}-\d{2})$', PricesListJSONView.as_view(), name="calendario_json_day"),
]
