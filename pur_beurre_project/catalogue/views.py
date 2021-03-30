import ast

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Sub_saved


def index(request):
    return render(request, 'catalogue/index.html')


def pagination(request, args, prods_max):
    paginator = Paginator(args, prods_max)
    page_number = request.GET.get('page', 1)

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page


def search(request):
    query = request.GET.get('query')
    if not query:
        messages.success(request, "Vous n'avez rien saisi")
        return redirect('home')
    else:
        products = Product.objects.filter(name__icontains=query)
        if not products.exists():
            context = {
                "no_product": True
            }
        else:
            context = {
                "query": query,
                "page": pagination(request, products, 6)
            }
        return render(request, 'catalogue/search.html', context)


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    categories = product.categories
    categories = ast.literal_eval(categories)
    order = Product.objects.filter(categories__icontains=categories)
    sub = order.order_by('nutriscore_grade', 'id')
    substitutes = []
    for x in sub:
        try:
            if x.name == product.name:
                substitutes.remove(x)
            if x.nutriscore_grade <= product.nutriscore_grade:
                substitutes.append(x)
        except:
            pass
    context = {
        "product": product,
        "query": product,
        "page": pagination(request, substitutes, 6),
    }
    return render(request, 'catalogue/detail.html', context)


@login_required
def save_in_db(request):
    if request.method == "POST":
        sub = request.POST.get('substitute')
        user = request.user
        try:
            save = Sub_saved.objects.filter(user=user.id,
                                            sub=sub.id)
            if not save:
                substitute = Sub_saved.objects.create(user=user.id,
                                         sub=sub.id)
                substitute.save()
                messages.success(request, 'Produit sauvegardé')
            else:
                messages.success(request, 'Le produit est déjà sauvegardé')

        finally:
            return redirect('catalogue:my_page')
    else:
        return redirect('home')


def legal_notice(request):
    return render(request, 'catalogue/legal-notice.html')


@login_required
def my_page(request):
    return render(request, 'catalogue/my_page.html')


@login_required
def my_products(request):
    return render(request, 'catalogue/my_products.html')
