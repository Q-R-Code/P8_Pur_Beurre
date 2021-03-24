import ast

import requests
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
    product_categories = ast.literal_eval(product.categories)
    url = f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&"
    for i in range(len(product_categories)):
        url += f"tagtype_{i}=categories&tag_contains_{i}=contains&tag_{i}={product_categories[i]}&"
    url += "page_size=100&json=true"
    req = requests.get(url)
    data = req.json()
    substitutes = []
    for x in range(100):
        score = data["products"][x].get("nutriscore_grade")
        if score == str("a"):
            substitutes.append(data["products"][x])
    if len(substitutes) == 0:
        for x in range(100):
            score = data["products"][x].get("nutriscore_grade")
            if score == str("b"):
                substitutes.append(data["products"][x])
    print(substitutes[0])
    context = {
        "product": product,
        "substitutes": substitutes
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
