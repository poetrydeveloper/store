from django.contrib import admin
from .models import Tools, Provider

class ToolsAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'provider', 'name','desc','created_at','updated_at',)
    list_display_links = ('id', 'code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('provider',)

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Tools, ToolsAdmin)
admin.site.register(Provider, ProviderAdmin)

