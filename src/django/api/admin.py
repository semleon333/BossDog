from django.contrib import admin
from .models import Warehouse, Products, ProductPhotos


class ProductPhotosAdmin(admin.StackedInline):
	model = ProductPhotos


class WarehouseAdmin(admin.ModelAdmin):
	fields_list = [field.name for field in Warehouse._meta.get_fields()].copy()     # get all fields from model
	list_display = fields_list[2:]  # exclude many-to-many and id fields
	list_display_links = ['name']
	search_fields = ('name',)


class ProductsAdmin(admin.ModelAdmin):
	fields_list = [field.name for field in Products._meta.get_fields()].copy()     # get all fields from model
	list_display = fields_list[2:-1]    # exclude foreign key fields
	list_display_links = ['name']
	search_fields = ('name', 'cost')
	filter_horizontal = ['materials']
	inlines = [ProductPhotosAdmin]


admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Products, ProductsAdmin)
# admin.site.register(ProductPhotos, ProductPhotosAdmin)
