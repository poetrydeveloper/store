from django.db import models

class Tools(models.Model):
    code = models.CharField(max_length=100, verbose_name='Артикул')
    name = models.TextField(max_length=250, verbose_name='Название')
    desc = models.TextField(max_length=250, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    provider = models.ForeignKey('Provider', on_delete=models.PROTECT, null=True, verbose_name='Поставщик')
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True, verbose_name='Бренд')
    # category= models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория', related_name='tools')
    tag = models.ManyToManyField('Tag', blank=True, related_name='tools', verbose_name='Тег')
    
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

# class Category(models.Model):
#     name = models.CharField(max_length=50, db_index=True, verbose_name='Категория')
#     slug = models.SlugField(max_length=250, verbose_name='Url', unique=True)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#         ordering = ['name']

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
        return f'{[self.created_at, self.quantity,]!r}'
    
    class Meta:
        verbose_name = 'ЗаказНаМагазин'
        verbose_name_plural = 'ЗаказыНаМагазин'
        ordering = ['-created_at']