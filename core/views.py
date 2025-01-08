from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def features(request):
    return render(request, 'core/features.html')

def pricing(request):
    return render(request, 'core/pricing.html')

def services(request):
    return render(request, 'core/products.html')