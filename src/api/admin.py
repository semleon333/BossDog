from django.contrib import admin
from . import models


class MaterialsAdmin(admin.ModelAdmin):
    pass


class MatAttributesAdmin(admin.ModelAdmin):
    fields = ['name', 'data_type', 'is_required', 'is_searchable']
    list_display = ['name', 'data_type']
    
    
#
# class ProductsAdmin(admin.ModelAdmin):
# 	fields_list = [field.name for field in Products._meta.get_fields()].copy()     # get all fields from model
# 	list_display = fields_list[2:-1]    # exclude foreign key fields
# 	list_display_links = ['name']
# 	search_fields = ('name', 'cost')
# 	filter_horizontal = ['materials']
# 	inlines = [ProductPhotosAdmin]
#
#
# admin.site.register(Materials, MaterialsAdmin)
# admin.site.register(Products, ProductsAdmin)
# admin.site.register(ProductPhotos, ProductPhotosAdmin)
admin.site.register(models.MatAttributes, MatAttributesAdmin)
# admin.site.register(models.Materials, MaterialsAdmin)
# admin.site.register(models.MatAttributes)
