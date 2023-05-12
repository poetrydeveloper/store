from django.db import models

class Tools(models.Model):
    code = models.CharField(max_length=100, verbose_name='Артикул')
    name = models.TextField(max_length=250, verbose_name='Название')
    desc = models.TextField(max_length=250, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    def __str__(self):
              return self.name
    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'
        