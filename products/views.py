# -*- coding: utf-8 -*-

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

	def get_queryset(self):
		""" Filtra resultados  """
		year = self.kwargs.get('year', False)
		month = self.kwargs.get('month', False)
		day = self.kwargs.get('day', False)
		week_day = self.kwargs.get('week', False)

		if year and month and day:
			return Price.objects.filter(is_public=True,
										date_start__year=year,
										date_start__month=month,
										date_start__day=day)

		if year and month:
			return Price.objects.filter(is_public=True,
										date_start__year=year,
										date_start__month=month)

		if year and week_day:
			return Price.objects.filter(is_public=True,
										date_start__year=year,
										date_start__week_day=week_day)

	def render_to_response(self, context, **response_kwargs):
		return self.render_to_json_response(self.object_list, **response_kwargs)