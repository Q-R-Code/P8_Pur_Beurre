from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    return render(request, 'catalogue/index.html')


def account(request):
    return render(request, 'catalogue/create_account.html')