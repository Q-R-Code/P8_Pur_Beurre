from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product


def index(request):
    return render(request, 'catalogue/index.html')


def search(request):
    query = request.GET.get('query')
    if not query:
        return redirect('/')
    else:
        products = Product.objects.filter(name__icontains=query)
        if not products.exists():
            context = {
                "no_product": True
            }
        else:
            context = {
                "products": products
            }
        return render(request, 'catalogue/search.html', context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product
    }
    return render(request, 'catalogue/detail.html', context)

def legal_notice(request):
    return render(request, 'catalogue/legal-notice.html')


@login_required
def my_page(request):
    return render(request, 'catalogue/my_page.html')


@login_required
def my_products(request):
    return render(request, 'catalogue/my_products.html')
