from django.contrib import admin
from .models import Order, OrderProducts
from product.models import ProductSKU
# Register your models here.
class OrderProductsInline(admin.TabularInline):
    model = OrderProducts
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','total_count','updated_time','created_time')
    inlines = [OrderProductsInline,]
    def save_formset(self, request, form, formset, change):
        formset.save()
        if not change:
            for f in formset.forms:
                obj = f.instance
                print(obj)
                print(obj.count)
                print(obj.sku.id)
                pro = ProductSKU.objects.get(id=obj.sku.id)
                pro.stock -= obj.count
                pro.save()
    search_fields = ('order_id',)


class OrderProductsAdmin(admin.ModelAdmin):
    list_display = ('__str__','sku','count')    
    search_fields = ('order__order_id','sku__product__name',)


admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProducts,OrderProductsAdmin)