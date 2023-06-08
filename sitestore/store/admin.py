from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ToolsAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'provider', 'brand', 'name','desc','created_at', 'get_photo','updated_at',)
    list_display_links = ('id', 'code', 'name')
    search_fields = ('code', 'name', 'brand')
    list_filter = ('provider', 'brand', )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src={obj.photo.url} width="100",  >')
        return '-'
        
    
    get_photo.short_description = 'изображение'

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class OrderStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at','updated_at','name','quantity', 'price',)
    list_display_links = ('id', 'created_at',)
    search_fields = ('code', 'quantity')
    list_filter = ('id', 'created_at',)

    def name(self, obj):
        return obj.tools
    name.short_description = u'название'

class DeliveryStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at','updated_at','name','quantity', 'price',)
    list_display_links = ('id', 'created_at',)
    search_fields = ('code', 'quantity')
    list_filter = ('id', 'created_at',)

    def name(self, obj):
        return obj.order.tools
    name.short_description = u'название'

class ManualDeliveryStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at','updated_at','name','quantity', 'price',)
    list_display_links = ('id', 'created_at',)
    search_fields = ('code', 'quantity')
    list_filter = ('id', 'created_at',)

    def name(self, obj):
        return obj.tools
    name.short_description = u'название'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at','updated_at', 'name', 'quantity', 'price',)
    list_display_links = ('id', 'created_at',)
    search_fields = ('code', 'quantity')
    list_filter = ('id', 'created_at',)

    def name(self, obj):
        if hasattr( obj.delivery, "order"):
            return obj.delivery.order.tools
        else:
            return obj.manual_delivery.tools
    name.short_description = u'название '


class P_CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at','updated_at', 'name', 'quantity', 'note',)
    list_display_links = ('id', 'created_at',)
    search_fields = ('quantity',)
    list_filter = ('id', 'created_at',)

    def name(self, obj):
        if hasattr( obj.products.delivery, "order"):
            return obj.products.delivery.order.tools
        else:
            return obj.products.manual_delivery.tools
    name.short_description = u'название '


class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at','updated_at', 'note', 'price')
    list_display_links = ('id', 'created_at',)
    search_fields = ('created_at',)
    list_filter = ('id', 'created_at',)


admin.site.register(Tools, ToolsAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(OrderStore, OrderStoreAdmin)
admin.site.register(DeliveryStore, DeliveryStoreAdmin)
admin.site.register(ManualDeliveryStore, ManualDeliveryStoreAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CollectionProducts, P_CollectionAdmin)
admin.site.register(Sales, SalesAdmin)
