from django.db import models
# import django.utils.timezone
from utils import models as utils_mod


class Metadata(models.Model):
    """Abstract class for metadata"""

    class AttribTypes(models.IntegerChoices):
        DATETIME = 1
        VARCHAR = 2
        TEXT = 3
        DECIMAL = 4
        INTEGER = 5
        PHOTO = 6

    data_type = models.IntegerField(choices=AttribTypes.choices)
    is_required = models.BooleanField("Обязательное поле?", default=False)
    is_searchable = models.BooleanField("Будет поиск по полю?", default=False)

    class Meta:
        abstract = True

class AttributeValuesDatetime(models.Model):
    """Атрибуты типа дата:время"""
    value = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

class AttributeValuesVarChar(models.Model):
    """Атрибуты типа небольшой текст"""
    value = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

class AttributeValueText(models.Model):
    """Атрибуты типа текст"""
    value = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

class AttributeValueDecimal(models.Model):
    """Атрибуты типа нецелое число"""
    value = models.DecimalField(
            max_digits=10, 
            decimal_places=2, 
            blank=True, 
            null=True,
    )

    class Meta:
        abstract = True

class AttributeValueInt(models.Model):
    """Атрибуты типа целое число"""
    value = models.IntegerField()

    class Meta:
        abstract = True

class AttributeValuePhoto(models.Model):
    """Атрибуты типа фото"""
    value = models.ImageField(upload_to=utils_mod.media_namer)

    class Meta:
        abstract = True

class Materials(models.Model):
    """Таблица с предметами на складе"""
    name = models.CharField('Название', max_length=256)
    count = models.IntegerField(default=0)
    reserved_count = models.IntegerField(default=0)
    discarded_count = models.IntegerField(default=0)
	
    class Meta:
        db_table = "materials"
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.name

class MatAttributes(Metadata):
    """Атрибуты материалов"""
    name = models.CharField('Название', max_length=256)

    class Meta:
        db_table = "material_attributes"
        verbose_name = "Хар-ка материала"
        verbose_name_plural = "Хар-ки материалов"

    def __str__(self):
        return self.name

class MatAttributeValueDatetime(AttributeValuesDatetime):
    """Атрибуты типа дата/время"""
    attribute_id = models.ForeignKey(
            MatAttributes, 
            on_delete=models.CASCADE,
    )
    entity_id = models.ForeignKey(
            Materials,
            on_delete=models.DO_NOTHING
    )

class MatAttributeValueText(AttributeValueText):
    """Атрибуты типа текст"""
    attribute_id = models.ForeignKey(
            MatAttributes, 
            on_delete=models.CASCADE,
    )
    entity_id = models.ForeignKey(
            Materials,
            on_delete=models.DO_NOTHING
    )

class MatAttributeValueDecimal(AttributeValueDecimal):
    """Атрибуты типа нецелое число"""
    attribute_id = models.ForeignKey(
            MatAttributes, 
            on_delete=models.CASCADE,
    )
    entity_id = models.ForeignKey(
            Materials,
            on_delete=models.DO_NOTHING
    )

class MatAttributeValueInt(AttributeValueInt):
    """Атрибуты типа целое число"""
    attribute_id = models.ForeignKey(
            MatAttributes, 
            on_delete=models.CASCADE,
    )
    entity_id = models.ForeignKey(
            Materials,
            on_delete=models.DO_NOTHING
    )

class MatAttributeValuePhoto(AttributeValuePhoto):
    """Атрибуты типа фото"""
    attribute_id = models.ForeignKey(
            MatAttributes, 
            on_delete=models.CASCADE,
    )
    entity_id = models.ForeignKey(
            Materials,
            on_delete=models.DO_NOTHING
    )

class Products(models.Model):
    """Таблица с каталогом товаров"""
    name = models.CharField('Название', max_length=256)
    materials = models.ManyToManyField(
            Materials,
            through='ProductMaterials'
    )

    class Meta:
        db_table = "products"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

class ProductMaterials(models.Model):
    """Таблица с материалами для товара"""
    products_id = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    materials_id = models.ForeignKey(Materials, on_delete=models.DO_NOTHING)
    count = models.IntegerField()

class ProdAttributes(Metadata):
    """Атрибуты товаров"""
    name = models.CharField('Название', max_length=256)

    class Meta:
        db_table = "products_attributes"
        verbose_name = "Хар-ка товара"
        verbose_name_plural = "Хар-ки товаров"

    def __str__(self):
        return self.name

class ProdAttribValuesDatetime(AttributeValuesDatetime):
    """Атрибуты типа дата/время"""
    attribute_id = models.ForeignKey(
            ProdAttributes, 
            on_delete=models.CASCADE,
    )
    entity_id = models.ForeignKey(
            Products,
            on_delete=models.DO_NOTHING
    )

class ProdAttributeValueText(AttributeValueText):
    """Атрибуты типа текст"""
    attribute_id = models.ForeignKey(
            ProdAttributes, 
            on_delete=models.CASCADE,
    )
    entity_id = models.ForeignKey(
            Products,
            on_delete=models.DO_NOTHING
    )

class ProdAttributeValueDecimal(AttributeValueDecimal):
    """Атрибуты типа нецелое число"""
    attribute_id = models.ForeignKey(
            ProdAttributes, 
            on_delete=models.CASCADE,
    )
    entity_id = models.ForeignKey(
            Products,
            on_delete=models.DO_NOTHING
    )

class ProdAttributeValueInt(AttributeValueInt):
    """Атрибуты типа целое число"""
    attribute_id = models.ForeignKey(
            ProdAttributes, 
            on_delete=models.CASCADE,
    )
    entity_id = models.ForeignKey(
            Products,
            on_delete=models.DO_NOTHING
    )

class ProdAttributeValuePhoto(AttributeValuePhoto):
    """Атрибуты типа фото"""
    attribute_id = models.ForeignKey(
            ProdAttributes, 
            on_delete=models.CASCADE,
    )
    entity_id = models.ForeignKey(
            Products,
            on_delete=models.DO_NOTHING
    )


# class Orders(models.Model):
# 	"""Таблица для заказов"""
# 	customer_id = models.IntegerField("Customer id")
# 	products = models.ManyToManyField(Products)

# 	ORDER_STATES = (
# 		(0, "Created"),
# 		(10, "In progress"),
# 		(20, "Waiting for dispatch"),
# 		(30, "Waiting for delivery"),
# 		(40, "Waiting to receive"),
# 		(50, "Closed"),
# 	)

# 	order_state = models.IntegerField("Состояние заказа", choices=ORDER_STATES)
# 	date_order_creation = models.DateTimeField("Дата создания заказа", default=django.utils.timezone.now())
# 	date_order_completed = models.DateField("Дата готовности заказа", blank=True, null=True)
# 	date_order_shipped = models.DateField("Дата отправки заказа", blank=True, null=True)
# 	date_order_arrived = models.DateField("Дата прибытия заказа", blank=True, null=True)
# 	date_order_received = models.DateField("Дата вручения заказа", blank=True, null=True)
# 	order_info = models.TextField("Описание заказа", blank=True, null=True)
# 	track_link = models.CharField("Ссылка для отслеживания", max_length=256, blank=True, null=True)

# 	class Meta:
# 		db_table = "orders"
# 		verbose_name = "Заказ"
# 		verbose_name_plural = "Заказы"

# 	def __str__(self):
# 		return self.pk

