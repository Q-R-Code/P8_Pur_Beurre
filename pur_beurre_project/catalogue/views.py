from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('catalogue/index.html')
    return HttpResponse(template.render(request=request))

def catalogue_test(request):
    message = "Test catalogue"
    return HttpResponse(message)