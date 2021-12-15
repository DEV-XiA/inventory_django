# Generated by Django 3.2.9 on 2021-11-18 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.IntegerField(choices=[(1, '颜色1'), (2, '颜色2'), (3, '颜色3'), (4, '颜色4')], verbose_name='颜色')),
                ('color_hex', models.CharField(default='#FFFFFF', max_length=7, verbose_name='HEX')),
            ],
            options={
                'verbose_name': '色彩管理',
                'verbose_name_plural': '色彩管理',
                'db_table': 'product_color',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='C+3', max_length=128, verbose_name='品牌')),
                ('name', models.CharField(max_length=20, verbose_name='商品名称')),
            ],
            options={
                'verbose_name': '商品SPU',
                'verbose_name_plural': '商品SPU',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'SMALL'), ('M', 'MEDIUM'), ('L', 'LARGE'), ('XL', 'EXTRA LARGE'), ('2XL', '2 EXTRA LARGE'), ('3XL', '3 EXTRA LARGE'), ('4XL', '4 EXTRA LARGE'), ('5XL', '5 EXTRA LARGE')], max_length=3, verbose_name='尺码')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('stock', models.IntegerField(default=0, verbose_name='库存数量')),
                ('available', models.BooleanField(default=True, verbose_name='上线')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.color', verbose_name='商品颜色')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='商品名称')),
            ],
            options={
                'verbose_name': '商品SKU',
                'verbose_name_plural': '商品SKU',
                'db_table': 'product_sku',
            },
        ),
        migrations.AddField(
            model_name='color',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='商品名称'),
        ),
    ]
