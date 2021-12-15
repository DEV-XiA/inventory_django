from django.db import models
from product.models import ProductSKU

# Create your models here.
# 定义订单模型        
    
class Order(models.Model):
    order_id = models.CharField(max_length=128, verbose_name='订单ID',default="")
    total_count = models.SmallIntegerField(default=1, verbose_name='商品数量')
    updated_time = models.DateTimeField(auto_now=True,verbose_name='更新日期')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    
    class Meta:
        db_table = 'order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return f'订单 [{self.order_id}]' 
    

# 定义订单商品模型

class OrderProducts(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    sku = models.ForeignKey(ProductSKU,on_delete=models.PROTECT,verbose_name='商品SKU')
    count = models.IntegerField(default=1, verbose_name='商品数量')
    

    def __str__(self):
        return str(self.order.order_id)
    
    class Meta:
        db_table = 'order_products'
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name