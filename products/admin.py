from django.contrib import admin

from products.models import Product, Photo, Price

class PriceInline(admin.TabularInline):
    model = Price

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        PriceInline,
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Photo)
admin.site.register(Price)