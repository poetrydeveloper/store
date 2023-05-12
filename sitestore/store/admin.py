from django.contrib import admin
from .models import Tools

class ToolsAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name','desc','created_at','updated_at',)
    list_display_links = ('id', 'code', 'name')
    search_fields = ('code', 'name')

admin.site.register(Tools, ToolsAdmin)

