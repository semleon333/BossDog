from django.db import models
from utils import models as utils_mod


class Warehouse(models.Model):
	"""Таблица с предметами на складе"""
	name = models.CharField('Название', max_length=256)
	color = models.CharField('Цвет', max_length=32, blank=True, null=True)
	material = models.CharField('Материал', max_length=64, blank=True, null=True)
	diameter = models.DecimalField('Диаметр, мм', max_digits=10, decimal_places=2, blank=True, null=True)
	length = models.DecimalField('Длина, мм', max_digits=10, decimal_places=2, blank=True, null=True)
	width = models.DecimalField('Ширина, мм', max_digits=10, decimal_places=2, blank=True, null=True)
	amount = models.IntegerField('Количество')
	
	class Meta:
		db_table = "warehouse"
		verbose_name = "Материал"
		verbose_name_plural = "Материалы"
	
	def __str__(self):
		if self.diameter and not (self.length or self.width):
			return f'{self.name}-{self.diameter}'
		if self.length and self.width:
			return f'{self.name}-{self.length}*{self.width}'
		else:
			return self.name


class Products(models.Model):
	"""Таблица с предлагаемыми товарами"""
	name = models.CharField('Название', max_length=256)
	description = models.TextField('Описание', blank=True, null=True)
	materials = models.ManyToManyField(Warehouse, verbose_name='Материалы')
	cost = models.DecimalField('Стоимость, руб.', max_digits=10, decimal_places=2, blank=True, null=True)
	
	class Meta:
		db_table = "products"
		verbose_name = "Товар"
		verbose_name_plural = "Товары"
	
	def __str__(self):
		return self.name

	
class ProductPhotos(models.Model):
	"""Таблица для фотографий товара"""
	fk = models.ForeignKey(Products, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=utils_mod.media_namer, verbose_name='Фото товара')

	class Meta:
		db_table = "product_photos"
		verbose_name = "Фото товара"
		verbose_name_plural = "Фотографии товара"

	def __str__(self):
		return "Фото товара"

# class Orders(models.Model):
# 	"""Таблица для заказов"""   # Нужно сделать, когда прикрутится телега для указателей на ID
