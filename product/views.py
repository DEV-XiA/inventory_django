from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductSKU

# Create your views here.
def inventory(request):
    products = ProductSKU.objects.all()
    context = {'products': products}
    return render(request, 'product/index.html',context)