from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.

def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')

def customer(request):
    return render(request, 'customer.html')
