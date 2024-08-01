from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import UpdateView
from .forms import ProductForm
from .models import Product

# Create your views here.

def landingPage(request):
    return render(request, 'base/landingPage.html')

@login_required(login_url='login')
def dashboard(request):
    products = Product.objects.filter(farmer = request.user).order_by('-created_at')
    return render(request, 'base/dashboard.html', { 'products' : products })

@login_required(login_url='login')
def homeView(request):
    products = Product.objects.all()
    
    return render(request, 'base/homePage.html', { 'products' : products })

@login_required(login_url='login')
def saveProduct(request):    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.farmer = request.user
            product.save()
            
            return redirect('dashboard')
    else:
        form = ProductForm()
    
    return render(request, 'base/newproduct.html', {'form' : form})

@login_required(login_url='login')
def deleteProduct(request, pk):
    product = Product.objects.get(id = pk)
    
    product.delete()
    return redirect('dashboard')

@login_required(login_url='login')
def detailsView(request, pk):
    product = Product.objects.get(id = pk)
    other_products = Product.objects.exclude(id = pk)
    
    return render(request, 'base/detailedView.html', {'product' : product, 'other_products' : other_products})

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'quantity', 'price', 'description', 'image']
    template_name = 'base/updateproduct.html'
    success_url = reverse_lazy('dashboard')