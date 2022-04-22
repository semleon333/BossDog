from django.db import models


class Warehouse(models.Model):
	"""Таблица с предметами на складе"""
	name = models.CharField('Название', max_length=256)
	color = models.CharField('Цвет(опц)', max_length=32, blank=True, null=True)
	material = models.CharField('Материал(опц)', max_length=64, blank=True, null=True)
	diameter = models.DecimalField('Диаметр(опц)', decimal_places=2, blank=True, null=True)
	length = models.DecimalField('Длина(опц)', decimal_places=2, blank=True, null=True)
	width = models.DecimalField('Ширина(опц)', decimal_places=2, blank=True, null=True)
	amount = models.IntegerField('Количество')
	
	class Meta:
		db_table = "warehouse"


class Products(models.Model):
	"""Таблица с предлагаемыми товарами"""
	name = models.CharField('Название', max_length=256)
	description = models.TextField('Описание', blank=True, null=True)
	materials = models.ManyToManyField('Warehouse')
	cost = models.DecimalField('Стоимость(опц)', decimal_places=2, blank=True, null=True)
	# image = models.ImageField() # DON'T FORGET TO CONFIG SIGNALS
	
	class Meta:
		db_table = "products"
