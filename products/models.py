# -*- coding: utf-8 -*-

from __future__ import unicode_literals

#from imagekit.models import ImageSpec
#from imagekit.processors import Crop

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class Photo(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=255, blank=True)
	original_image = models.ImageField(upload_to='images')
	date_added = models.DateTimeField(auto_now_add=True)
	is_public = models.BooleanField(default=True)
	#thumbnail = models.ImageSpec([Crop(60, 60)], image_field='original_image')

	class Meta:
		ordering = ['-date_added']
		get_latest_by = 'date_added'
		verbose_name = _("photo")
		verbose_name_plural = _("photos")

	def __str__(self):
		return self.title


class Product(models.Model):
	name = models.CharField(max_length=200, blank=False, null=False)
	description = models.CharField(max_length=200, blank=False, null=False)
	images = models.ManyToManyField(Photo, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	is_public = models.BooleanField(default=True)

	class Meta:
		ordering = ['-date_added']
		get_latest_by = 'date_added'
		verbose_name = _("product")
		verbose_name_plural = _("products")

	def __str__(self):
		return self.name


class Price(models.Model):
	product = models.ForeignKey(Product)
	date = models.DateField()
	hour_start = models.TimeField()
	hour_end = models.TimeField()
	price_from = models.DecimalField(max_digits=5, decimal_places=2)
	price_to = models.DecimalField(max_digits=5, decimal_places=2)
	is_public = models.BooleanField(default=True)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = (("product", "date", "hour_start", "hour_end"))
		ordering = ['-date']
		get_latest_by = 'id'
		verbose_name = _("price")
		verbose_name_plural = _("prices")

	def __str__(self):
		return "%s, de %.2f por %.2f em %s as %s ate %s" % (self.product, self.price_from,
															self.price_to, self.date,
															self.hour_start, self.hour_end)