from unicodedata import name
from django.contrib import admin
from .models import Product, ProductSKU, Color
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'brand')
    search_fields = ('name',)


class ProductSKUAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'color','size','updated_time','created_time','stock','available')
    list_editable = ('stock', 'available')
    search_fields = ('product__name',)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('product', 'color', 'color_hex','colored_show')
    search_fields = ('product__name',)

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductSKU,ProductSKUAdmin)
admin.site.register(Color,ColorAdmin)

admin.site.site_title = "QUTUEU库存管理"
admin.site.site_header = "QUTUEU库存管理"
