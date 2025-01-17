from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    return render(request, 'third_task/index.html')

def store(request):
    return render(request, 'third_task/store.html')

def cart(request):
    return render(request, 'third_task/cart.html')