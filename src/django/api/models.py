from django.db import models
import django.utils.timezone
from utils import models as utils_mod


class Tags(models.Model):
	"""Таблица с тэгами товаров и заказов"""
	name = models.CharField("Имя тэга", max_length=64)


class Materials(models.Model):
	"""Таблица с предметами на складе"""
	name = models.CharField('Название', max_length=256)
	color = models.CharField('Цвет', max_length=32, blank=True, null=True)
	material = models.CharField('Материал', max_length=64, blank=True, null=True)
	inner_diameter = models.DecimalField('Внутренний иаметр, мм', max_digits=10, decimal_places=2, blank=True, null=True)
	outer_diameter = models.DecimalField('Внешний диаметр, мм', max_digits=10, decimal_places=2, blank=True, null=True)
	length = models.DecimalField('Длина, мм', max_digits=10, decimal_places=2, blank=True, null=True)
	width = models.DecimalField('Ширина, мм', max_digits=10, decimal_places=2, blank=True, null=True)
	amount = models.IntegerField('Количество')
	tags = models.ManyToManyField(Tags)

	class Meta:
		db_table = "materials"
		verbose_name = "Материал"
		verbose_name_plural = "Материалы"

	def __str__(self):
		if (self.inner_diameter and self.outer_diameter) and not (self.length or self.width):
			return f'{self.name}-{self.inner_diameter}{self.outer_diameter}'
		if self.length and self.width:
			return f'{self.name}-{self.length}*{self.width}'
		else:
			return self.name


class Products(models.Model):
	"""Таблица с предлагаемыми товарами"""
	name = models.CharField('Название', max_length=256)
	description = models.TextField('Описание', blank=True, null=True)
	materials = models.ManyToManyField(Materials, verbose_name='Материалы')
	cost = models.DecimalField('Стоимость, руб.', max_digits=10, decimal_places=2, blank=True, null=True)
	tags = models.ManyToManyField(Tags, verbose_name="Тэги")

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


class Orders(models.Model):
	"""Таблица для заказов"""
	customer_id = models.IntegerField("Customer id")
	products = models.ManyToManyField(Products)

	ORDER_STATES = (
		(0, "Created"),
		(10, "In progress"),
		(20, "Waiting for dispatch"),
		(30, "Waiting for delivery"),
		(40, "Waiting to receive"),
		(50, "Closed"),
	)

	order_state = models.IntegerField("Состояние заказа", choices=ORDER_STATES)
	date_order_creation = models.DateTimeField("Дата создания заказа", default=django.utils.timezone.now())
	date_order_completed = models.DateField("Дата готовности заказа", blank=True, null=True)
	date_order_shipped = models.DateField("Дата отправки заказа", blank=True, null=True)
	date_order_arrived = models.DateField("Дата прибытия заказа", blank=True, null=True)
	date_order_received = models.DateField("Дата вручения заказа", blank=True, null=True)
	order_info = models.TextField("Описание заказа", blank=True, null=True)
	track_link = models.CharField("Ссылка для отслеживания", max_length=256, blank=True, null=True)
	tags = models.ManyToManyField(Tags)

	class Meta:
		db_table = "orders"
		verbose_name = "Заказ"
		verbose_name_plural = "Заказы"

	def __str__(self):
		return self.pk


class ReservedMaterials(models.Model):
	"""Таблица, куда переносятся зарезервированные материалы"""
	order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
	material_id = models.ForeignKey(Materials, on_delete=models.CASCADE)
	amount = models.IntegerField('Количество')

	class Meta:
		db_table = "reserved_materials"
		verbose_name = "Зарезервированные материалы"
		verbose_name_plural = "Зарезервированные материалы"

	# def __str__(self):
	# 	if self.diameter and not (self.length or self.width):
	# 		return f'{self.name}-{self.diameter}'
	# 	if self.length and self.width:
	# 		return f'{self.name}-{self.length}*{self.width}'
	# 	else:
	# 		return self.name
