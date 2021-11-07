from django.db import models
from django.db.models.enums import Choices

# 定义产品类
class Product(models.Model):

    COLOR_NUMBERS = [
        (1,'颜色1'),
        (2,'颜色2'),
        (3,'颜色3'),
        (4,'颜色4'),
        ]

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

    name = models.CharField(max_length=100)
    color = models.IntegerField(choices=COLOR_NUMBERS)
    size = models.CharField(choices=SIZES, max_length=3)
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField(default=0)
    color_hex = models.CharField(max_length=7,default='#FFFFFF')
    
    def __str__(self):
        return self.name + '-' + str(self.color)
    
