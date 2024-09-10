from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ['id','frist_name', 'last_name', 'phone', 'email', 'created_at']
    search_fields = ['frist_name', 'last_name', 'phone', 'email']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
    ordering = ['created_at']
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ['frist_name', 'last_name']
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['id']