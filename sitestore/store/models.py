from django.db import models
from mptt.models import MPTTModel, TreeForeignKey



class MainPage(models.Model):
    
    def __str__(self):
              return self.name


class CollectionProducts(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    products = models.ForeignKey('Product', on_delete=models.PROTECT, blank=True, verbose_name='Продукт')
    note = models.TextField(max_length=250, blank=True, verbose_name='Примечание', null=True)
    quantity = models.PositiveIntegerField(null=True, verbose_name='Количество в магазине.')

    def __str__(self):
        return f'Ед.т.: {self.products.delivery.order.tools.name}, {self.quantity}шт.'
    
    class Meta:
        verbose_name = 'Добавленный товар в магазин.'
        verbose_name_plural = 'Добавленные товары в магазин.'
        ordering = ['created_at']

class Tools(models.Model):
    code = models.CharField(max_length=100, verbose_name='Артикул')
    name = models.TextField(max_length=250, verbose_name='Название')
    desc = models.TextField(max_length=250, blank=True, verbose_name='Описание', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    provider = models.ForeignKey('Provider', on_delete=models.PROTECT, null=True, verbose_name='Поставщик')
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True, verbose_name='Бренд')
    category= TreeForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория', related_name='cat')
    tag = models.ManyToManyField('Tag', blank=True, related_name='tag', verbose_name='Тег')
    
    def __str__(self):
              return self.name
    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'

class Provider(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Поставщик')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['name']

class Brand(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Бренд')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ['name']

class Category(MPTTModel):
    name = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='Категория')
    slug = models.SlugField(max_length=250, verbose_name='Url', unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родительский класс')

    def __str__(self):
        return self.name
    
    class MPTTMeta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        order_insertion_by = ['name']

class Tag(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Тег')
    slug = models.SlugField(max_length=250, verbose_name='Tag', unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

class Store(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Тег')
    slug = models.SlugField(max_length=250, verbose_name='Tag', unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['name']

class OrderStore(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    quantity = models.PositiveIntegerField(null=True, verbose_name='Количество')
    price = models.FloatField(blank=True, verbose_name='Цена')
    tools = models.ForeignKey('Tools', on_delete=models.PROTECT, blank=True, verbose_name='Товар')

    def __str__(self):
        return f'{self.created_at.date()} - {self.tools}, {self.quantity}шт.'
    
    class Meta:
        verbose_name = 'заказ на магазин'
        verbose_name_plural = 'заказы на магазин'
        ordering = ['-created_at']

class DeliveryStore(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    quantity = models.PositiveIntegerField(null=True, verbose_name='Количество')
    price = models.FloatField(blank=True, verbose_name='Цена')
    order = models.OneToOneField('OrderStore', on_delete=models.PROTECT, blank=True, verbose_name='Заказ')

    def __str__(self):
        return f'{self.created_at.date()} - {self.order.tools.name}, {self.quantity}шт.'
    
    class Meta:
        verbose_name = 'поставка на магазин'
        verbose_name_plural = 'поставки на магазин'
        ordering = ['-created_at']

class ManualDeliveryStore(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    quantity = models.PositiveIntegerField(null=True, verbose_name='Количество')
    price = models.FloatField(blank=True, verbose_name='Цена')
    tools = models.ForeignKey('Tools', on_delete=models.PROTECT, blank=True, verbose_name='Товар')

    def __str__(self):
        return f'Ручная - {self.created_at.date()} - {self.tools}, {self.quantity}шт.'
    
    class Meta:
        verbose_name = 'ручная поставка на магазин'
        verbose_name_plural = 'ручные поставки на магазин'
        ordering = ['-created_at']

class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    icode = models.TextField(max_length=250, verbose_name='внутренний код',null=True,blank=True,)
    delivery = models.OneToOneField('DeliveryStore', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Заказ')
    manual_delivery = models.OneToOneField('ManualDeliveryStore', on_delete=models.PROTECT, blank=True,null=True, verbose_name='ручной заказ')
    quantity = models.PositiveIntegerField(null=True, verbose_name='Количество')
    price = models.FloatField(blank=True, verbose_name='Цена')

    def __str__(self):
        return f'Продукт - {self.created_at.date()} - , {self.quantity}шт.'
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']


class Sales(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    code_record = models.TextField(max_length=250, verbose_name='код записи',null=True,blank=True,)
    price = models.FloatField(blank=True, verbose_name='Цена продажи')
    note = models.TextField(max_length=250, blank=True, verbose_name='Примечание', null=True)
    products = models.ForeignKey('Product', on_delete=models.PROTECT, blank=True, verbose_name='Продукт')

    def __str__(self):
        return f'Продажа - {self.created_at.date()} '
    
    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'
        ordering = ['created_at']