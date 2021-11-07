from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__','color','color_hex','size','updated_time','created_time','number')


admin.site.register(Product,ProductAdmin)

admin.site.site_title = "QUTUEU库存管理"
admin.site.site_header = "QUTUEU库存管理"
