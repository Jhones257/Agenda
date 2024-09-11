from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name', 'phone', 'email', 'created_at', 'show']
    search_fields = ['first_name', 'last_name', 'phone', 'email']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
    ordering = ['created_at']
    list_per_page = 10
    list_max_show_all = 100
    list_editable = ['show']
    list_display_links = ['first_name', 'last_name']
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['id']