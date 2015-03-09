from django.shortcuts import render
from lib2to3.fixes.fix_input import context
from .models import Product

# Create your views here.
def home(request):
    
    if request.user.is_authenticated():
        username_is = "Matt using context"
        context = {"username_is": request.user}   # or just request.user
    else:
        context = {"username_is": request.user}
        
    template = 'products/home.html'
    return render(request, template, context)
    
    
def all(request):
    
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)


    
    