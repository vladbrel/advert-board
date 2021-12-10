from django.contrib import admin
from .models import Ad, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} #по name делает автоматически slug

admin.site.register(Category, CategoryAdmin)

class AdAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price']
    list_filter = ['created', 'updated']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Ad, AdAdmin)


