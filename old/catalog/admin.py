from django.contrib import admin


# Register your models here.

class CatalogAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'date', 'image']
