from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def homepage(request):
    products= Product.objects.all()

    data = {
        'products': products
    }
    return render(request, 'home.html', data)

def aboutpage(request):
    return render(request, 'about.html')