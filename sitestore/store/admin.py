from django.contrib import admin
from .models import Tools, Provider, Brand, Tag
from django.utils.safestring import mark_safe

class ToolsAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'provider', 'brand', 'name','desc','created_at', 'get_photo','updated_at',)
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

admin.site.register(Tools, ToolsAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Brand, BrandAdmin)
# admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)

