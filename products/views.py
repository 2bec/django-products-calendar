# -*- coding: utf-8 -*-

import datetime

from django.views.generic.dates import DayArchiveView, WeekArchiveView, MonthArchiveView
from django.views.generic.list import ListView

from products.models import Price
from products.mixins import JSONResponseMixin


class PricesDayArchiveView(DayArchiveView, JSONResponseMixin):
	""" Lista de precos em um determinado dia """
	#queryset = Price.objects.all()
	template_name = "products/price_archive_day.html"
	date_field = "date_start"
	month_format = "%m"
	allow_future = True
	allow_empty = True

	def get_queryset(self):
		""" Somente os precos que sao publicos """
		return Price.objects.filter(is_public=True)

	def get_context_data(self, **kwargs):
		context = super(PricesDayArchiveView, self).get_context_data(**kwargs)
		context["year"] = year = self.kwargs.get('year', "2016")
		context["month"] = month = self.kwargs.get('month', "1")
		context["day"] = day = self.kwargs.get('day', "1")
		return context

	def render_to_response(self, context):
		# Look for a 'format=json' GET argument
		if self.request.GET.get('format') == 'json':
			return self.render_to_json_response(self.object_list)
		else:
			return super(PricesDayArchiveView, self).render_to_response(context)


class PricesWeekArchiveView(WeekArchiveView, JSONResponseMixin):
	""" Lista de precos de uma semana """
	#queryset = Price.objects.all()
	template_name = "products/price_archive_week.html"
	date_field = "date_start"
	week_format = "%W"
	allow_future = True
	allow_empty = True

	def get_queryset(self):
		""" Somente os precos que sao publicos """
		return Price.objects.filter(is_public=True)

	def get_context_data(self, **kwargs):
		context = super(PricesWeekArchiveView, self).get_context_data(**kwargs)
		context["year"] = year = self.kwargs.get('year', "2016")
		context["week"] = week = self.kwargs.get('week', "1")
		return context

	def render_to_response(self, context):
		# Look for a 'format=json' GET argument
		if self.request.GET.get('format') == 'json':
			return self.render_to_json_response(self.object_list)
		else:
			return super(PricesWeekArchiveView, self).render_to_response(context)


class PricesMonthArchiveView(MonthArchiveView, JSONResponseMixin):
	""" Lista de precos de um mês """
	#queryset = Price.objects.all()
	template_name = "products/price_archive_month.html"
	date_field = "date_start"
	month_format = "%m"
	allow_future = True
	allow_empty = True

	def get_queryset(self):
		""" Somente os precos que sao publicos """
		return Price.objects.filter(is_public=True)

	def get_context_data(self, **kwargs):
		context = super(PricesMonthArchiveView, self).get_context_data(**kwargs)
		context["year"] = year = self.kwargs.get('year', "2016")
		context["month"] = month = self.kwargs.get('month', "1")
		return context

	def render_to_response(self, context):
		# Look for a 'format=json' GET argument
		if self.request.GET.get('format') == 'json':
			return self.render_to_json_response(self.object_list)
		else:
			return super(PricesMonthArchiveView, self).render_to_response(context)


class PricesListJSONView(JSONResponseMixin, ListView):

	model = Price

	#def get_date_from_week(self, year, week):
	#	new_date = datetime.date(year,1,1)
	#	new_date = new_date - datetime.timedelta(new_date.weekday())
	#	week_date = datetime.timedelta(days = (week)*7)
	#	return new_date + week_date #for range,  new_date + week_date + datetime.timedelta(days=6)

	def get_queryset(self):
		""" Filtra resultados usando kwargs """
		date_start = datetime.datetime.strptime(self.kwargs.get('date_start', 0), '%Y-%m-%d')
		date_end = datetime.datetime.strptime(self.kwargs.get('date_end', 0), '%Y-%m-%d')

		return Price.objects.filter(
				is_public=True,
				date_start__range=(
					datetime.datetime.combine(date_start, datetime.time.min),
					datetime.datetime.combine(date_end, datetime.time.max)
				)
		)

	def render_to_response(self, context, **response_kwargs):
		return self.render_to_json_response(self.object_list, **response_kwargs)