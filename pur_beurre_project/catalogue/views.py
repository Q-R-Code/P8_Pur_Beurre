from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'catalogue/index.html')

def legal_notice(request):
    return render(request, 'catalogue/legal-notice.html')

@login_required
def my_page(request):
    return render(request, 'catalogue/my_page.html')

@login_required
def my_products(request):
    return render(request, 'catalogue/my_products.html')
