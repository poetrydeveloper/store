from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ToolsAdminForm(forms.ModelForm):
    name = forms.CharField(widget=CKEditorUploadingWidget())
    desc = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Tools
        fields = '__all__'

class ToolsAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'provider', 'brand', 'name','desc','created_at', 'get_photo','updated_at',)
    form = ToolsAdminForm
    list_display_links = ('id', 'code', 'name')
    search_fields = ('code', 'name', 'brand')
    list_filter = ('provider', 'brand', )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" wigth="50">')
        return '-'
    
    get_photo.short_description = 'фото'

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ("name",)}
#     list_display = ('id', 'name',)
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)

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
    list_display = ('id', 'created_at','updated_at','quantity', 'price',)
    list_display_links = ('id', 'created_at',)
    search_fields = ('code', 'quantity')
    list_filter = ('id', 'created_at',)

class DeliveryStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at','updated_at','quantity', 'price',)
    list_display_links = ('id', 'created_at',)
    search_fields = ('code', 'quantity')
    list_filter = ('id', 'created_at',)

class ManualDeliveryStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at','updated_at','quantity', 'price',)
    list_display_links = ('id', 'created_at',)
    search_fields = ('code', 'quantity')
    list_filter = ('id', 'created_at',)

admin.site.register(Tools, ToolsAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Brand, BrandAdmin)
# admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(OrderStore, OrderStoreAdmin)
admin.site.register(DeliveryStore, DeliveryStoreAdmin)
admin.site.register(ManualDeliveryStore, ManualDeliveryStoreAdmin)

