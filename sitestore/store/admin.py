from django.contrib import admin
from .models import Tools, Provider, Brand

class ToolsAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'provider', 'brand', 'name','desc','created_at','updated_at',)
    list_display_links = ('id', 'code', 'name')
    search_fields = ('code', 'name', 'brand')
    list_filter = ('provider', 'brand')

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Tools, ToolsAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Brand, BrandAdmin)

