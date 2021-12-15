from itertools import product
from tabnanny import verbose
from django.db import models
from django.utils.html import format_html

# 定义产品模型

class Product(models.Model):
    brand = models.CharField(max_length=128,default='C+3',verbose_name='品牌')
    name = models.CharField(max_length=20, verbose_name='商品名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = '商品SPU'
        verbose_name_plural = verbose_name

class Color(models.Model):

    COLOR_NUMBERS = [
    (1,'颜色1'),
    (2,'颜色2'),
    (3,'颜色3'),
    (4,'颜色4'),
    ]

    product = models.ForeignKey(Product,on_delete=models.PROTECT,verbose_name='商品名称')
    color = models.IntegerField(choices=COLOR_NUMBERS,verbose_name='颜色')
    color_hex = models.CharField(max_length=7,default='#FFFFFF',verbose_name='HEX')

    def __str__(self):
        return self.product.name + '-' + str(self.color) 

    def colored_show(self):
        return format_html(
            # f'<span style="color: {self.color_hex};">{self.color_hex}</span>',
             f'<div style="width:80px; height:20px; background-color:{ self.color_hex }"></div>'
        ) 

    class Meta:
        db_table = 'product_color'
        verbose_name = '色彩管理'
        verbose_name_plural = verbose_name


# 定义产品sku模型  
      
class ProductSKU(models.Model):

    SIZES = [
        ('S','SMALL'),
        ('M','MEDIUM'),
        ('L','LARGE'),
        ('XL','EXTRA LARGE'),
        ('2XL','2 EXTRA LARGE'),
        ('3XL','3 EXTRA LARGE'),
        ('4XL','4 EXTRA LARGE'),
        ('5XL','5 EXTRA LARGE'),
    ]

    product = models.ForeignKey(Product,on_delete=models.PROTECT,verbose_name='商品名称')
    color = models.ForeignKey(Color,on_delete=models.PROTECT,verbose_name='商品颜色')
    size = models.CharField(choices=SIZES, max_length=3,verbose_name='尺码')
    updated_time = models.DateTimeField(auto_now=True,verbose_name='更新日期')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    stock = models.IntegerField(default=0,verbose_name='库存数量')
    available = models.BooleanField(default=True,verbose_name='上线')
    
    
    def __str__(self):
        return self.product.name + '-' + str(self.color.color) + '-' + str(self.size)


    class Meta:
        db_table = 'product_sku'
        verbose_name = '商品SKU'
        verbose_name_plural = verbose_name

